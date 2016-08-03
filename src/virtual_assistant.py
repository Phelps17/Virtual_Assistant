from weather.weather_controller import *
from events.date_time_controller import *
from config.user import *
from reply_controller import *
from config.config_at_launch import *

# Basic API Functions:
#	- calendar
#	- email
#	- facebook
#	- twitter
# Desired API Functions:
#	- recent news
#	- wolfram alpha

# Test calls
reply = ReplyController()
weather = WeatherController()
user = load_user()
clock = DateTimeController()

print reply.good_morning(user)
print reply.good_afternoon(user)
print reply.good_night(user)
user.set_formality_level(1)
print reply.good_morning(user)
print reply.good_afternoon(user)
print reply.good_night(user)
user.set_formality_level(2)
print reply.good_morning(user)
print reply.good_afternoon(user)
print reply.good_night(user)

print weather.get_current_conditions(user.get_location())

print clock.get_time() + " " + clock.get_date()