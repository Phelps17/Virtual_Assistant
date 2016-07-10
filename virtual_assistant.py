from weather_controller import *
from date_time_controller import *
from user import *
from reply_controller import *

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
user = User("Tyler", "Phelps", "MALE", "Chicago", 0)
print reply.good_night(user)
user.set_formality_level(1)
print reply.good_night(user)
user.set_formality_level(2)
print reply.good_night(user)