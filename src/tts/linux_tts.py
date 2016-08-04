import pyttsx

class LinuxSpeechToText :
	def __init__(self) :
		self.engine = pyttsx.init()

	def say(self, text) :
		engine.say(text)
		engine.runAndWait()
