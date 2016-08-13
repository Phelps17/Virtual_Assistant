
class InputController :
	def __init__(self, input_mode) :
		self.input_mode = input_mode

	def get_input(self) :
		# get the input from either cmd or mic
		if (self.input_mode == 0) :
			#print "command arguments"
			return
		elif (self.input_mode == 1) :
			#print "voice arguments (not implemented)"
			return
		else :
			#print "default (command arguments)"
			return

	def process_input(self, input_string) :
		# figure out what command to run
		# return the command name in a string array
		# string at 0 and args after that
		pass