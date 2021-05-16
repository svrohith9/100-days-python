from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
item_a_tag = soup.findAll("a", class_="storylink")
score_span_tag = soup.findAll("span", class_="score")

item_list_text = [i.getText() for i in item_a_tag]
item_list_url = [i.get("href") for i in item_a_tag]

item_upvote_list = [int(str(i.getText()).split(" ")[0])
                    for i in score_span_tag]

# item_data = list(zip(item_list_text, item_list_url, item_upvote_list))
index_val = item_upvote_list.index(max(item_upvote_list))
print(index_val)
print(item_upvote_list.pop(index_val))
print(item_list_text.pop(index_val))
