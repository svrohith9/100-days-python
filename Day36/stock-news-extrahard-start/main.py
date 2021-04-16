import requests

STOCK = "AAPL"
COMPANY_NAME = "Apple Inc"

STOCK_API = "https://www.alphavantage.co/query"
STOCK_API_KEY =  # KEY


NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY =  # KEY

# TWILIO_API =
# TWILIO_API_KEY =

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}


stock_api_call = requests.get(url=STOCK_API, params=stock_params)
stock_api_call.raise_for_status()
stock_response = stock_api_call.json()["Time Series (Daily)"]
stock_price_list = [value for key, value in stock_response.items()]

yesterday_close_price = stock_price_list[0]["4. close"]
day_before_yesterday = stock_price_list[1]["4. close"]

price_diff = abs(float(yesterday_close_price) - float(day_before_yesterday))
diff_prcnt = (price_diff/float(yesterday_close_price))*100


if diff_prcnt >= 1.2:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }

    news_api_call = requests.get(url=NEWS_API, params=news_params)
    news_api_call.raise_for_status()
    news_api_response = news_api_call.json()["articles"][:3]
    print(news_api_response)
