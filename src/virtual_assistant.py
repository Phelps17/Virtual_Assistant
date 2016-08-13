from weather.weather_controller import *
from events.date_time_controller import *
from config.user import *
from reply_controller import *
from config.config_at_launch import *
from tts.mac_tts import *
from tts.linux_tts import *
from tts.no_tts import *
from input_controller import *

# In Progress API Functions:
#	- facebook
#	- twitter
# Future API Functions:
#	- calendar
#	- email
#	- recent news
#	- alarms

# ================ SET UP ================
reply = ReplyController()
weather = WeatherController()
user = load_user()
clock = DateTimeController()
voice = NoTextToSpeech()
io = InputController(0)

if user.get_system_type() == 'MAC' :
	voice = MacTextToSpeech()
elif user.get_system_type() == 'LINUX' :
	voice = LinuxTextToSpeech()

user.set_formality_level(2)
# ========================================

io.get_input()

#while (1) :
	# get input
	# run command