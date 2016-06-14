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
	def __init__(self, parsed_json, location_string) :
		self.location_string = location_string
		self.forecast_list = list()
		self.parsed_json = parsed_json

		if (parsed_json is None) :
			self.is_populated = False
		else :
			self.is_populated = True
			self.parsed_json = self.parsed_json
			self.city = self.parsed_json["query"]["results"]["channel"]["location"]["city"]
			self.country = self.parsed_json["query"]["results"]["channel"]["location"]["country"]
			self.region = self.parsed_json["query"]["results"]["channel"]["location"]["region"]

			self._add_forecast_days()

	def get_current_conditions(self) :
		if (self.is_populated) :
			title = self.parsed_json["query"]["results"]["channel"]["item"]["title"]
			temp = self.parsed_json["query"]["results"]["channel"]["item"]["condition"]["temp"]
			condition = self.parsed_json["query"]["results"]["channel"]["item"]["condition"]["text"]
			units = self.parsed_json["query"]["results"]["channel"]["units"]["temperature"]

			return title+"\n"+temp+units+" & "+condition
		else :
			return "error"

	def get_forecast_conditions(self) :
		return self.forecast_list

	def _add_forecast_days(self):
		#for (day in self.parsed_json["query"]["results"]["channel"]["item"]["forecast"]) :
			#next_forecast = ForecastedWeatherObject(day["date"], day["day"], day["high"], day["low"], day["text"])
			#self.forecast_list.add(next_forecast)

		for i in range(0,10) :
			date = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["date"]
			day = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["day"]
			high = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["high"]
			low = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["low"]
			text = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["text"]
			self.forecast_list.insert(i, ForecastedWeatherObject(date, day, high, low, text))
