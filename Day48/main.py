from selenium import webdriver

driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.python.org/")

times = driver.find_elements_by_css_selector(
    ".event-widget time")
# li is used to avoid the extra element "more"
names = driver.find_elements_by_css_selector(
    ".event-widget li a")

events = {}

for n in range(len(names)):
    events[n] = {
        "name": names[n].text,
        "time": times[n].text
    }

print(events)

driver.quit()
