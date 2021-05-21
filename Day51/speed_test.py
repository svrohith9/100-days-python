from selenium import webdriver
import time


class InternetSpeedTwitterBot:
    def __init__(self):
        driver_path = "D:\chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)
        self.down_speed = 0

    def get_internet_speed(self):
        self.driver.get("https://fast.com")
        time.sleep(10)
        self.down_speed = self.driver.find_element_by_id("speed-value")
        return int(self.down_speed.text)

    def tweet_at_provider(self, username, password):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        twitter_username = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        twitter_password = self.driver.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        submit = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
        # print(username, '::::::::::::', password)
        twitter_username.send_keys(username)
        twitter_password.send_keys(password)
        submit.click()

        time.sleep(5)
        # create tweet
        tweet = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet.send_keys(f"God Damn it {self.down_speed.text}")
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()
