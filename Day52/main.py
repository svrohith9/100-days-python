from insta import InstaFollower

USERNAME = "USERNAME HERE"
PASSWORD = "PASSWORD HERE"
SIMILAR_ACCOUNT = "ufc"

insta = InstaFollower()
insta.login(username=USERNAME, password=PASSWORD)
insta.find_followers(acct=SIMILAR_ACCOUNT)
insta.follow()
