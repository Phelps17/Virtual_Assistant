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
			title = self.get_current_title()
			temp = self.get_current_temp()
			condition = self.get_current_condition_text()
			units = self.get_temp_units()

			return title+"\n"+temp+units+" & "+condition
		else :
			return "error"

	def get_current_title(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["item"]["title"]
		else :
			return "error"

	def get_current_temp(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["item"]["condition"]["temp"]
		else :
			return "error"

	def get_current_condition_text(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["item"]["condition"]["text"]
		else :
			return "error"

	def get_temp_units(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["units"]["temperature"]
		else :
			return "error"

	def get_distance_units(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["units"]["distance"]
		else :
			return "error"

	def get_pressure_units(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["units"]["pressure"]
		else :
			return "error"

	def get_speed_units(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["units"]["speed"]
		else :
			return "error"

	def get_weather_on_day(self) :
		if (self.is_populated) :
			#TODO Add get weather conditions from certain forecast day
			pass
		else :
			return "error"

	def get_forecast_conditions(self) :
		return self.forecast_list

	def _add_forecast_days(self):
		for i in range(0,10) :
			date = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["date"]
			day = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["day"]
			high = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["high"]
			low = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["low"]
			text = self.parsed_json["query"]["results"]["channel"]["item"]["forecast"][i]["text"]
			self.forecast_list.insert(i, ForecastedWeatherObject(date, day, high, low, text))

	def get_sunrise_time(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["units"]["temperature"]
		else :
			return "error"

	def get_sunset_time(self) :
		pass

	#TODO get sunrise time
	#TODO get sunset time
	#TODO get time at location

query, results, channel, units,		
"""
{
   "query": {
      "count": 1,
      "created": "2016-07-07T04:19:24Z",
      "lang": "en",
      "results": {
         "channel": {
            "location": {
               "city": "Madison",
               "country": "United States",
               "region": " WI"
            },
            "wind": {
               "chill": "73",
               "direction": "250",
               "speed": "7"
            },
            "atmosphere": {
               "humidity": "83",
               "pressure": "977.0",
               "rising": "0",
               "visibility": "16.1"
            },
            "astronomy": {
               "sunrise": "5:25 am",
               "sunset": "8:39 pm"
            },
            "item": {
               "title": "Conditions for Madison, WI, US at 10:00 PM CDT",
               "lat": "43.072948",
               "long": "-89.386688",
               "condition": {
                  "code": "29",
                  "date": "Wed, 06 Jul 2016 10:00 PM CDT",
                  "temp": "74",
                  "text": "Partly Cloudy"
               },
         }
      }
   }
}
"""
