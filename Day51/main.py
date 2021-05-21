from speed_test import InternetSpeedTwitterBot

twitter_email = "YOUR EMAIL"
twitter_password = "YOUR PASSWORD"
down_speed = 50

twitter_bot = InternetSpeedTwitterBot()
# print(twitter_bot.get_internet_speed())

if twitter_bot.get_internet_speed() < down_speed:
    twitter_bot.tweet_at_provider(
        username=twitter_email, password=twitter_password)
