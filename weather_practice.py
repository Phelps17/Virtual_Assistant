import urllib2
import json
import numpy

class Weather :
	def __init__(self) :
		return

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

	def get_current_conditions(self, location) :
		json_string = self.get_weather_json(location)
		parsed_json = self.parse_weather_json(json_string)
		title = parsed_json["query"]["results"]["channel"]["item"]["title"]
		temp = parsed_json["query"]["results"]["channel"]["item"]["condition"]["temp"]
		condition = parsed_json["query"]["results"]["channel"]["item"]["condition"]["text"]
		units = parsed_json["query"]["results"]["channel"]["units"]["temperature"]

		return title+"\n"+temp+units+" & "+condition

	
while (1) :
	weather = Weather()
	input = raw_input("Enter a location: ")
	if input == "end" :
		exit()
	else:
		current_conditions = weather.get_current_conditions(input)
		print current_conditions