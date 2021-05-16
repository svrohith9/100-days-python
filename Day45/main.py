from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
item_a_tag = soup.find("a", class_="storylink")
item_name = item_a_tag.getText()
item_link = item_a_tag.get("href")

score_span_tag = soup.find("span", class_="score")
item_upvote = score_span_tag.getText()

print("item Name: ", item_name)
print("item Link: ", item_link)
print("item Score: ", item_upvote)
