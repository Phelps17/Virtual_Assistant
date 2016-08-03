from user import *

def load_user() :
	config_file = open("config/user_info.conf", 'r')
	user = User("", "", "", "", 0)

	for line in config_file:
		config_data = line.strip().replace(" ", "").split("=")
		
		key = config_data[0]
		value = config_data[1]

		if key == 'FIRSTNAME' :
			user.set_first_name(value);
		elif key == 'LASTNAME' :
			user.set_last_name(value)
		elif key == 'GENDER' :
			user.set_gender(value)
		elif key == 'LOCATION' :
			user.set_location(value)
		elif key == 'FORMALITY_LEVEL' :
			user.set_formality_level(int(value))
		elif key == 'FACEBOOK_ACTIVATED' :
			user.set_is_facebook_activated(bool(value))
		elif key == 'FACEBOOK_AUTH_TOKEN' :
			user.set_facebook_token(value)
		elif key == 'TWITTER_ACTIVATED' :
			user.set_is_twitter_activated(bool(value))
		elif key == 'TWITTER_CONSUMER_KEY' :
			user.set_twitter_ct(value)
		elif key == 'TWITTER_CONSUMER_SECRET' :
			user.set_twitter_cs(value)
		elif key == 'TWITTER_ACCESS_TOKEN' :
			user.set_twitter_at(value)
		elif key == 'TWITTER_ACCESS_TOKEN_SECRET' :
			user.set_twitter_as(value)
		else :
			print key
			print "Invalid argument in config file."

	config_file.close()

	return user

