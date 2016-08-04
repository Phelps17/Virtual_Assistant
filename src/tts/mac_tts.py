from os import system

class MacTextToSpeech :
	def __init__(self) :
		return

	def say(self, text) :
		sys_call = "say " + text
		system(sys_call)
