from weather.weather_controller import *
from events.date_time_controller import *
from config.user import *
from reply_controller import *
from config.config_at_launch import *
from tts.mac_tts import *
from tts.linux_tts import *
from tts.no_tts import *

# In Progress API Functions:
#	- calendar
#	- email
#	- facebook
#	- twitter
#	- recent news

# Test calls
reply = ReplyController()
weather = WeatherController()
user = load_user()
clock = DateTimeController()
voice = NoTextToSpeech()

if user.get_system_type() == 'MAC' :
	voice = MacTextToSpeech()
elif user.get_system_type() == 'LINUX' :
	voice = LinuxTextToSpeech()

user.set_formality_level(2)
voice.say(reply.hello(user))
voice.say(reply.good_bye(user))
voice.say(reply.thank_you(user))
voice.say(reply.youre_welcome(user))
voice.say(reply.yes(user))
voice.say(reply.no(user))
voice.say(reply.sorry(user))
voice.say(reply.can_i_help_you(user))
voice.say(reply.good_morning(user))
voice.say(reply.good_afternoon(user))
voice.say(reply.good_night(user))

voice.say("It is currently " + weather.get_current_temp(user.get_location()) + " and " + weather.get_current_condition_text(user.get_location()) + " in " + user.get_location() + ".")
voice.say(clock.get_time() + " " + clock.get_date())
