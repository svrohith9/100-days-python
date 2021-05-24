import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

FORM_URL = "https://forms.gle/FUxNvvYGnP9MWQXN6"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.69044004359946%2C%22north%22%3A37.86004559039139%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9"
}


response = requests.get(ZILLOW_URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

span_all_address = soup.findAll(
    "address", class_="list-card-addr")

all_address = [address.getText() for address in span_all_address]
# print(len(all_address))

div_all_prices = soup.findAll("div", class_="list-card-price")
# removed $, ',' and other texts "+1b" converted to int
try:
    all_prices = [int(price.getText()[1:6].replace(',', ''))
                  for price in div_all_prices]
except:
    print("Error Converting prices from the page")
finally:
    print("All houses prices converted to int values")
# print(len(all_prices))

a_all_urls = soup.findAll(
    "a", class_="list-card-img", href=True)
all_urls = [a['href'] for a in a_all_urls]
all_links = []
for url in all_urls:
    if "http" not in url:
        all_links.append(f"https://www.zillow.com{url}")
    else:
        all_links.append(url)
# print(len(all_links))

# saving data into form via selenium automation

driver_path = "D:/chromedriver.exe"
driver = webdriver.Chrome(driver_path)

driver.get(FORM_URL)


def add_data(addr, li, pr):
    time.sleep(1)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/textarea')
    address.send_keys(addr)

    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(pr)

    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(li)

    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()


def refresh():
    time.sleep(1)
    new_response = driver.find_element_by_link_text("Submit another response")
    new_response.click()


for i in range(0, len(all_prices)):
    add_data(addr=all_address[i],
             li=all_links[i], pr=all_prices[i])
    refresh()
    print("Done")
