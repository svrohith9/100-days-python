from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    def __init__(self):
        driver_path = "D:\chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usr = self.driver.find_element_by_name("username")
        pwd = self.driver.find_element_by_name("password")

        usr.send_keys(username)
        pwd.send_keys(password)

        submit = self.driver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div')
        submit.click()

    def find_followers(self, acct):
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{acct}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath(
                    '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
