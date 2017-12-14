import urllib.request
import json

getWeather = urllib.request.urlopen('http://api.wunderground.com/api/1acc3b86d3ed81e6/geolookup/conditions/q/CT/West_Hartford.json')
json_string = getWeather.read()
currentWeather = json.loads(json_string)
locationState = currentWeather['location']['state']
locationCity = currentWeather['location']['city']
currentTemp = currentWeather['current_observation']['temp_f']
currentCondition = currentWeather['current_observation']['weather']
getWeather.close()
print("It is %s degrees with an %s" % (currentTemp, currentCondition))
