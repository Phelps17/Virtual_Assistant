
class InputController :
	def __init__(self, input_mode) :
		self.input_mode = input_mode

	def get_input(self) :
		# get the input from either cmd or mic
		if (self.input_mode == 0) :
			return raw_input()
		elif (self.input_mode == 1) :
			print "voice arguments (not implemented)"
			return
		else :
			return raw_input()

	def process_input(self, input_string) :
		print input_string
		
		# nltk split up sentence for keywords and arguments
		# try to find super keys
		# cross refernce found keywords with cached commands
		# cross reference with non-cached keywords
		# determine the command to be ran
		# determine the arguments and types of arguments needed
		# determine those arguments
		# order command and args into a strng array
		# return that array

		pass