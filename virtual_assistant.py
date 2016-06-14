from weather_controller import *


weather = WeatherController()

while (1) :
	input = raw_input("Enter a location: ")
	if input == "end" :
		exit()
	else:
		current_conditions = weather.get_current_conditions(input)
		print current_conditions

		forecast_conditions = weather.get_forecast_conditions(input)
		for i in range(0, len(forecast_conditions)) :
			print forecast_conditions[i].day+", "+forecast_conditions[i].date
			print "High: "+forecast_conditions[i].high+"\tLow: "+forecast_conditions[i].low
			print forecast_conditions[i].text
			print