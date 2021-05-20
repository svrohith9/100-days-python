from selenium import webdriver

driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

print(count.text)

driver.quit()
