USER_INFO_CONFIG_FILE = "user_info.conf"

class User() :
	#FORMALITY LEVEL:
	# 0) Casual
	# 1) Semi-formal
	# 2) Formal

	def __init__(self, first_name, last_name, gender, location, formality_level) :
		self.first_name = first_name
		self.last_name = last_name
		self.gender = gender
		self.location = location
		self.formality_level = formality_level

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

	def set_full_name(self) :
		full_name = first_name + " " + last_name

	def set_formality_level(self, new_level) :
		self.formality_level = new_level

	def get_prefix(self) :
		if (self.gender is "MALE") :
			return "Mr."
		elif (self.gender is "FEMALE") :
			return "Ms."
		else :
			return self.first_name

	def get_formal_title(self) :
		if (self.gender is "MALE") :
			return "Sir"
		elif (self.gender is "FEMALE") :
			return "Ma'am"
		else :
			return self.first_name
