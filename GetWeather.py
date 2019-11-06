# ===========================================================================
# Get Weather Data From api.openweathermap.org
#
# ===========================================================================
import json
import requests
from datetime import datetime
import common

url = "http://api.openweathermap.org/data/2.5/forecast?q=Melbourne,AU&units=metric&APPID=e79c59d54b437abefcab039dd2657f5c"

response = requests.get(url)
# ===========================================================================
# API Status Code
# 200: Everything went okay, and the result has been returned (if any).
# 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
# 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
# 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
# 403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
# 404: The resource you tried to access wasn’t found on the server.
# 503: The server is not ready to handle the request.
# ===========================================================================

#print(response.text[:1000])
#print( type(response.text))

#common.jprint(response.json())

todayWeather = {}

# json.load() - Takes a JSON string, and converts(loads) it to a Python object
jsonFormat = json.loads(response.text)
print( jsonFormat["list"][0]["weather"][0]["main"])
print( jsonFormat["list"][0]["weather"][0]["description"])
print( jsonFormat["list"][0]["main"]["temp_min"])
print( jsonFormat["list"][0]["main"]["temp_max"])
print( jsonFormat["list"][0]["main"]["humidity"])
print( jsonFormat["list"][0]["wind"]["speed"])
print( jsonFormat["city"]["sunrise"])
print( jsonFormat["city"]["sunset"])

todayWeather["Description"] = jsonFormat["list"][0]["weather"][0]["description"]
todayWeather["Temp_min"] = jsonFormat["list"][0]["main"]["temp_min"]
todayWeather["Temp_max"] = jsonFormat["list"][0]["main"]["temp_max"]
todayWeather["Humidity"] = jsonFormat["list"][0]["main"]["humidity"]
todayWeather["Wind_speed"] = jsonFormat["list"][0]["wind"]["speed"]
todayWeather["Sunrise"] = jsonFormat["city"]["sunrise"]
todayWeather["Sunset"] = jsonFormat["city"]["sunset"]
todayWeather["Icon"] = jsonFormat["list"][0]["weather"][0]["icon"]

# test for datetime
sunrise = jsonFormat["city"]["sunrise"]
timezone = jsonFormat["city"]["timezone"]
sunset = jsonFormat["city"]["sunset"]

time = datetime.fromtimestamp(sunrise)
todayWeather["Str_sunrise"] = str(time)
print("Sunrise: " , time)
time = datetime.fromtimestamp(sunset)
print("Sunset:  " , time)
todayWeather["Str_sunset"] = str(time)

# Weather Icon URL
# http://openweathermap.org/img/wn/04n.png
print( "Weather ICON URL: http://openweathermap.org/img/wn/" + todayWeather["Icon"] + ".png" )
todayWeather["Icon"] = "http://openweathermap.org/img/wn/" + todayWeather["Icon"] + ".png"

#print( todayWeather )
common.jprint( todayWeather )
# Write json to TodayWeather.json file
fout = open("TodayWeather.json", "w")
#fout.write(str(todayWeather))

# using json.dump to store json format to file
# json.dump() - Takes in a Python object, and converts(dumps) it to a string
json.dump(todayWeather, fout, sort_keys=True, indent=2 )

fout.close()
