from random import randint

#TODO adjust based on frequency
#TODO adjust based on time of day

class ReplyController :
	def __init__(self) :
		return

	def hello(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			return "Hey, " + str(user.get_first_name()) + "."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "Hello, " + str(user.get_first_name()) + "."
			elif (response_choice is 1) :
				return "Hello, " + str(user.get_prefix()) + " " + str(user.get_last_name()) + "."
			else :
				return "Hello, " + str(user.get_first_name()) + "."
		else :
			return "Greetings " + str(user.get_prefix()) + " " + str(user.get_last_name()) + "."

	def good_bye(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			return "Talk to you later!"
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "Good bye, " + str(user.get_first_name()) + "."
			elif (response_choice is 1) :
				return "Good bye, " + str(user.get_prefix()) + " " + str(user.get_last_name()) + "."
			else :
				return "Good bye, " + str(user.get_first_name()) + "."
		else :
			return "Farewell " + user.get_formal_title() + "."

	def thank_you(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return "Thank you."
			elif (response_choice is 1) :
				return "Thank you."
			else :
				return "Thank you."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "Thank you."
			elif (response_choice is 1) :
				return "Thank you."
			else :
				return "Thank you."
		else :
			if (response_choice is 0) :
				return "Thank you."
			elif (response_choice is 1) :
				return "Thank you."
			else :
				return "Thank you."

	def youre_welcome(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return "You're Welcome."
			elif (response_choice is 1) :
				return "Of course."
			else :
				return "No problem."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "You're Welcome."
			elif (response_choice is 1) :
				return "My pleasure."
			else :
				return "It's my pleasure."
		else :
			if (response_choice is 0) :
				return "My pleasure, " + user.get_formal_title() + "."
			elif (response_choice is 1) :
				return "My pleasure, " + user.get_formal_title() + "."
			else :
				return "My pleasure, " + user.get_formal_title() + "."

	def yes(self, user) :
		return "Yes."

	def no(self, user) :
		return "No."

	def sorry(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return "Sorry, " + user.get_first_name() + "."
			elif (response_choice is 1) :
				return "Sorry, " + user.get_first_name() + "."
			else :
				return "Sorry, " + user.get_first_name() + "."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "I'm sorry, " + user.get_prefix() + " " + user.get_last_name() + "."
			elif (response_choice is 1) :
				return "My apologies, " + user.get_prefix() + " " + user.get_last_name() + "."
			else :
				return "I'm sorry, " + user.get_prefix() + " " + user.get_last_name() + "."
		else :
			if (response_choice is 0) :
				return "My apologies, " + user.get_formal_title() + "."
			elif (response_choice is 1) :
				return "Please forgive me, " + user.get_formal_title() + "."
			else :
				return "My apologies, " + user.get_formal_title() + "."

	def can_i_help_you(self, user) :
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			return "How can I help you?"
		elif (formality_level is 1) :
			return "How can I help you?"
		else :
			return "How can I help you?"

	def good_morning(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return "Good morning, " + user.get_first_name() + "."
			elif (response_choice is 1) :
				return "Good morning, " + user.get_first_name() + "."
			else :
				return "Good morning, " + user.get_first_name() + "."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "Good morning, " + user.get_prefix() + " " + user.get_last_name() + "."
			elif (response_choice is 1) :
				return "Good morning, " + user.get_prefix() + " " + user.get_last_name() + "."
			else :
				return "Good morning, " + user.get_prefix() + " " + user.get_last_name() + "."
		else :
			if (response_choice is 0) :
				return "Good morning, " + user.get_formal_title() + "."
			elif (response_choice is 1) :
				return "Good morning, " + user.get_formal_title() + "."
			else :
				return "Good morning, " + user.get_formal_title() + "."

	def good_afternoon(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return "Good afternoon, " + user.get_first_name() + "."
			elif (response_choice is 1) :
				return "Good afternoon, " + user.get_first_name() + "."
			else :
				return "Good afternoon, " + user.get_first_name() + "."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "Good afternoon, " + user.get_prefix() + " " + user.get_last_name() + "."
			elif (response_choice is 1) :
				return "Good afternoon, " + user.get_prefix() + " " + user.get_last_name() + "."
			else :
				return "Good afternoon, " + user.get_prefix() + " " + user.get_last_name() + "."
		else :
			if (response_choice is 0) :
				return "Good afternoon, " + user.get_formal_title() + "."
			elif (response_choice is 1) :
				return "Good afternoon, " + user.get_formal_title() + "."
			else :
				return "Good afternoon, " + user.get_formal_title() + "."

	def good_night(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return "Good night, " + user.get_first_name() + "."
			elif (response_choice is 1) :
				return "Good night, " + user.get_first_name() + "."
			else :
				return "Good night, " + user.get_first_name() + "."
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return "Good night, " + user.get_prefix() + " " + user.get_last_name() + "."
			elif (response_choice is 1) :
				return "Good night, " + user.get_prefix() + " " + user.get_last_name() + "."
			else :
				return "Good night, " + user.get_prefix() + " " + user.get_last_name() + "."
		else :
			if (response_choice is 0) :
				return "Good night, " + user.get_formal_title() + "."
			elif (response_choice is 1) :
				return "Good night, " + user.get_formal_title() + "."
			else :
				return "Good night, " + user.get_formal_title() + "."

	def _diversify_response(self) :
		return randint(0,2)