import numpy
import json

class ForecastedWeatherObject() :
	def __init__(self, date, day, high, low, text) :
		self.date = date
		self.day = day
		self.high = high
		self.low = low
		self.text = text

class WeatherObject :
	def __init__(self, parsed_json) :
		if (parsed_json is None) :
			self.is_populated = False
		else :
			self.is_populated = True
			self.parsed_json = parsed_json

	def get_current_conditions(self) :
		if (self.is_populated) :
			title = self.parsed_json["query"]["results"]["channel"]["item"]["title"]
			temp = self.parsed_json["query"]["results"]["channel"]["item"]["condition"]["temp"]
			condition = self.parsed_json["query"]["results"]["channel"]["item"]["condition"]["text"]
			units = self.parsed_json["query"]["results"]["channel"]["units"]["temperature"]

			return title+"\n"+temp+units+" & "+condition
		else :
			return "error"


	def add_forecast_day(self):
		pass