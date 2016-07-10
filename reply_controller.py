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
			if (response_choice is 0) :
				return 
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def good_bye(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def thank_you(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def youre_welcome(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def yes(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def no(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def sorry(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def can_i_help_you(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def good_morning(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

	def good_afternoon(self, user) :
		response_choice = self._diversify_response()
		formality_level = user.get_formality_level()
		if (formality_level is 0) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		elif (formality_level is 1) :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return
		else :
			if (response_choice is 0) :
				return
			elif (response_choice is 1) :
				return
			else :
				return

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