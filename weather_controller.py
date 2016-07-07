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

	def _check_if_location_needs_update(self, location):
		if (self.weather_object.is_populated is not True) :
			self._update_weather_object(location)
		elif (self.weather_object.location_string != location) :
			if (len(location) > 0) :
				self._update_weather_object(location)

	def get_current_conditions(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_current_conditions()

	def get_forecast_conditions(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_forecast_conditions()

	def get_current_title(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_current_title()

	def get_current_temp(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_current_temp()

	def get_current_condition_text(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_current_condition_text()

	def get_temp_units(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_temp_units()

	def get_distance_units(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_pressure_units()

	def get_pressure_units(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.)

	def get_speed_units(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_speed_units()

	def get_weather_on_day(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_weather_on_day()

	def get_sunrise_time(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_sunrise_time()

	def get_sunset_time(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_sunset_time()

	def get_wind_chill(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_wind_chill()

	def get_wind_direction(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_wind_direction()

	def get_wind_speed(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_wind_speed()

	def get_atmosphere_humidity(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_atmosphere_humidity()

	def get_atmosphere_pressure(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_atmosphere_pressure()

	def get_atmosphere_rising(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_atmosphere_rising()

	def get_atmosphere_visibility(self, location) :
		self._check_if_location_needs_update(location)
		return self.weather_object.get_atmosphere_visibility()





