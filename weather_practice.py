import urllib2
import json

def get_weather_json(location) :

	location = location.replace(" ", ",%")
	url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + location + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
	
	#TODO catch url errors here
	json_string = urllib2.urlopen(url).read()
	return json_string

def parse_weather_json(json_string) :
	parsed_json = json.loads(json_string)

	#TODO check for parsing errors
	return parsed_json

def get_current_conditions(parsed_json) :
	title = parsed_json["query"]["results"]["channel"]["item"]["title"]
	temp = parsed_json["query"]["results"]["channel"]["item"]["condition"]["temp"]
	condition = parsed_json["query"]["results"]["channel"]["item"]["condition"]["text"]
	units = parsed_json["query"]["results"]["channel"]["units"]["temperature"]

	return title+"\n"+temp+units+" & "+condition

while (1) :
	input = raw_input("Enter a location: ")
	if input == "end" :
		exit()
	else:
		print get_current_conditions(parse_weather_json(get_weather_json(input)))