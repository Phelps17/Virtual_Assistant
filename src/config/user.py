USER_INFO_CONFIG_FILE = "user_info.conf"

class User :
	#FORMALITY LEVEL:
	# 0) Casual
	# 1) Semi-formal
	# 2) Formal

	def __init__(self, first_name, last_name, gender, location, formality_level) :
		# basic info
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.location = location
		self.formality_level = formality_level
		# social media auth info
		self.facebook_active = False
		self.twitter_active = False
		self.facebook_token = ""
		self.twitter_ct = ""
		self.twitter_cs = ""
		self.twitter_at = ""
		self.twitter_as = ""
		# Text to speech
		self.system_type = "UNKNOWN"

	def get_first_name(self) :
		return self.first_name

	def get_last_name(self) :
		return self.last_name

	def get_gender(self) :
		return self.gender

	def get_location(self) :
		return self.location

	def get_formality_level(self) :
		return self.formality_level

	def set_first_name(self, new_name) :
		self.first_name = new_name

	def set_last_name(self, new_name) :
		self.last_name = new_name

	def set_gender(self, new_gender) :
		self.gender = new_gender

	def set_location(self, new_location) :
		self.location = new_location

	def get_full_name(self) :
		full_name = first_name + " " + last_name
		return full_name

	def set_formality_level(self, new_level) :
		self.formality_level = new_level

	def get_prefix(self) :
		if (self.gender == "MALE") :
			return "Mr."
		elif (self.gender == "FEMALE") :
			return "Ms."
		else :
			return self.first_name

	def get_formal_title(self) :
		if (self.gender == "MALE") :
			return "Sir"
		elif (self.gender == "FEMALE") :
			return "Ma'am"
		else :
			return self.first_name

	def set_is_facebook_activated(self, bool_input) :
		if (bool_input is True) :
			self.facebook_active = True
		else :
			self.facebook_active = False

	def set_is_twitter_activated(self, bool_input) :
		if (bool_input is True) :
			self.twitter_active = True
		else :
			self.twitter_active = False

	def get_is_facebook_activated(self) :
		return self.facebook_active

	def get_is_twitter_activated(self) :
		return self.twitter_active

	def set_facebook_token(self, token) :
		self.facebook_token = token

	def set_twitter_ct(self, val) :
		self.twitter_ct = val

	def set_twitter_cs(self, val) :
		self.twitter_cs = val

	def set_twitter_at(self, val) :
		self.twitter_at = val

	def set_twitter_as(self, val) :
		self.twitter_as = val

	def get_facebook_token(self) :
		return self.facebook_token

	def get_twitter_ct(self) :
		return self.twitter_ct

	def get_twitter_cs(self) :
		return self.twitter_cs

	def get_twitter_at(self) :
		return self.twitter_at

	def get_twitter_as(self) :
		return self.twitter_as

	def set_system_type(self, sys_type) :
		self.system_type = sys_type

	def get_system_type(self) :
		return self.system_type