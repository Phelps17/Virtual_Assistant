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
			return self.parsed_json["query"]["results"]["channel"]["astronomy"]["sunrise"]
		else :
			return "error"

	def get_sunset_time(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["astronomy"]["sunset"]
		else :
			return "error"

	def get_wind_chill(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["wind"]["chill"]
		else :
			return "error"

	def get_wind_direction(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["wind"]["direction"]
		else :
			return "error"

	def get_wind_speed(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["wind"]["speed"]
		else :
			return "error"

	def get_atmosphere_humidity(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["atmosphere"]["humidity"]
		else :
			return "error"

	def get_atmosphere_pressure(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["atmosphere"]["pressure"]
		else :
			return "error"

	def get_atmosphere_rising(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["atmosphere"]["rising"]
		else :
			return "error"

	def get_atmosphere_visibility(self) :
		if (self.is_populated) :
			return self.parsed_json["query"]["results"]["channel"]["atmosphere"]["visibility"]
		else :
			return "error"