from bs4 import BeautifulSoup
import requests
import smtplib
import ssl

# Get amazon product page using requests.get

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
    "Accept-Language": "en-GB,en;q=0.9"
}

amazon_iphone_url = "https://www.amazon.in/New-Apple-iPhone-11-128GB/dp/B08L8BJ9VC/ref=sr_1_3?dchild=1&keywords=iphone&qid=1621382317&sr=8-3"

response = requests.get(url=amazon_iphone_url, headers=headers)
response.raise_for_status()

# Extract the price from the response
soup = BeautifulSoup(response.text, 'html.parser')
span_price = soup.find(
    "span", class_="a-size-medium a-color-price priceBlockBuyingPriceString")

# extract the price
# Since the price of the item is 59,999 at this time,
# Generic assumption:
# price cannot go down below 1,999, hence i am extracting "59" from the "₹ 59,999.00"
# triggering an alert if price goes below 40 which is "₹ 40,999.00"

amazon_iphone_price = float((str(span_price.getText()).split(",")[0][2:]))

# print(amazon_iphone_price)

if(amazon_iphone_price <= 40):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "my@gmail.com"
    receiver_email = "your@gmail.com"
    password = "your password"
    message = """\
    Subject: Hi there
    Your Product price if Dropped Below ₹ 40,999.00
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
