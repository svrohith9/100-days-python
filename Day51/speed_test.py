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
        return self.down_speed.text

    def tweet_at_provider(self, username, password):
        self.driver.get("https://twitter.com/login")
