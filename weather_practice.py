import urllib2

def get_weather_json(location) :

	location = location.replace(" ", "%")
	url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22" + location + "%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
	
	#TODO catch url errors here
	json = urllib2.urlopen(url).read()
	return json


get_weather_json("Madison, WI")