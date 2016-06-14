import urllib2
import json
import numpy
from weather_object import *

class WeatherController:
	def __init__(self) :
		self.weather_object = WeatherObject(None, "Empty")

	def _get_weather_json(self, location) :
		location = location.replace(" ", ",%")
		url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + location + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
		
		#TODO catch url errors here
		json_string = urllib2.urlopen(url).read()
		return json_string

	def _parse_weather_json(self, json_string) :
		parsed_json = json.loads(json_string)

		#TODO check for parsing errors
		return parsed_json

	def _update_weather_object(self, location) :
		json_string = self._get_weather_json(location)
		parsed_json = self._parse_weather_json(json_string)
		self.weather_object = WeatherObject(parsed_json, location)

	def get_current_conditions(self, location) :
		if (self.weather_object.is_populated is not True) :
			self._update_weather_object(location)
		elif (self.weather_object.location_string != location) :
			if (len(location) > 0) :
				self._update_weather_object(location)

		return self.weather_object.get_current_conditions()

	def get_forecast_conditions(self, location) :
		if (self.weather_object.is_populated is not True) :
			self._update_weather_object(location)
		elif (self.weather_object.location_string != location) :
			if (len(location) > 0) :
				self._update_weather_object(location)

		return self.weather_object.get_forecast_conditions()






