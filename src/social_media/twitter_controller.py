import tweepy

CONSUMER_KEY = "your key here"
CONSUMER_SECRET = "your key here"
ACCESS_TOKEN = "your key here"
ACCESS_TOKEN_SECRET = "your key here"

class TwitterController :
	def __inti__(self) :
		auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
		auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		self.api = tweepy.API(auth)

	def get_timeline_tweets(self) :
		return api.home_timeline()

	def get_my_tweets(self) :
		pass

	def get_tweets_of_user(self, other_username) :
		account_name = self._get_user_twitter_name(other_username)
		pass

	def _get_user_twitter_name(self, other_user_name) :
		pass

	def tweet(self, tweet) :
		pass