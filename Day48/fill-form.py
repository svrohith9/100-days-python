from selenium import webdriver

driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
last_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
first_name.send_keys("abcd")
last_name.send_keys("abcd")
email.send_keys("abcd@abcd.com")
# since there is only one button
submit = driver.find_element_by_tag_name("button")
submit.click()
