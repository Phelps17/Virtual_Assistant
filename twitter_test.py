import tweepy

CONSUMER_KEY = "your key here"
CONSUMER_SECRET = "your key here"
ACCESS_TOKEN = "your key here"
ACCESS_TOKEN_SECRET = "your key here"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text + "\n"
