USER_INFO_CONFIG_FILE = "user_info.conf"

class User() :
	def __inti__(self) :
		self.first_name = ""
		self.last_name = ""
		self.gender = ""
		self.location = ""
		self.formality_level = ""
		self._parse_user_info_config()

	def _parse_user_info_config(self) :
		return

	def get_first_name(self) :
		return self.first_name

	def get_last_name(self) :
		return self.last_name

	def get_gender(self) :
		return self.gender

	def get_location(self) :
		return self.location

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
