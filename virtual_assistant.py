from weather_controller import *


weather = WeatherController()

while (1) :
	input = raw_input("Enter a location: ")
	if input == "end" :
		exit()
	else:
		current_conditions = weather.get_current_conditions(input)
		print current_conditions