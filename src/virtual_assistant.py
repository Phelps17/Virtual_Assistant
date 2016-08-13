from weather.weather_controller import *
from events.date_time_controller import *
from config.user import *
from reply_controller import *
from config.config_at_launch import *
from tts.mac_tts import *
from tts.linux_tts import *
from tts.no_tts import *
from input_controller import *

KILL_STRING = "die" #TODO - add to config

def cleanup_and_exit() :
	exit()

def run_command() :
	pass

# ================ SET UP ================
reply = ReplyController()
weather = WeatherController()
user = load_user()
clock = DateTimeController()
voice = NoTextToSpeech()
io = InputController(0) #TODO - add to config

if user.get_system_type() == 'MAC' :
	voice = MacTextToSpeech()
elif user.get_system_type() == 'LINUX' :
	voice = LinuxTextToSpeech()

user.set_formality_level(2) #TODO - add to config
# ========================================

while (1) :
	# get input
	input_string = io.get_input()
	if (input_string == KILL_STRING) :
		cleanup_and_exit()
	else :
		io.process_input(input_string)
		run_command()

exit()