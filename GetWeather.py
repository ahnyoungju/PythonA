# ***************************************************************************
# * Get Weather Data From api.openweathermap.org
# *
# * By Youngju Ahn(100546460)
# ***************************************************************************
import json
import requests
from datetime import datetime
import common

# URL to read weather information
location = "Melbourne"
api_id = "e79c59d54b437abefcab039dd2657f5c"
url = "http://api.openweathermap.org/data/2.5/forecast?q=" + location + ",AU&units=metric&APPID=" + api_id

# request weather data
response = requests.get(url)
# ***************************************************************************
# API Status Code
# 200: Everything went okay, and the result has been returned (if any).
# 301: The server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
# 400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
# 401: The server thinks you’re not authenticated. Many APIs require login ccredentials, so this happens when you don’t send the right credentials to access an API.
# 403: The resource you’re trying to access is forbidden: you don’t have the right permissions to see it.
# 404: The resource you tried to access wasn’t found on the server.
# 503: The server is not ready to handle the request.
# ***************************************************************************

# response is not 200, something is wrong.
if response.status_code != 200:
    print("Can't get weather details. Check " + url )
    print("\nAPI Status Code: ", response.status_code)
    exit(-1)

# json.load() - Takes a JSON string, and converts(loads) it to a Python object
# jsonFormat = json.loads(response.text)
jsonResponse = response.json()
todayWeather = {}
todayWeather["Description"] = jsonResponse["list"][0]["weather"][0]["description"]
todayWeather["Temp_min"] = jsonResponse["list"][0]["main"]["temp_min"]
todayWeather["Temp_max"] = jsonResponse["list"][0]["main"]["temp_max"]
todayWeather["Humidity"] = jsonResponse["list"][0]["main"]["humidity"]
todayWeather["Wind_speed"] = jsonResponse["list"][0]["wind"]["speed"]
todayWeather["Sunrise"] = jsonResponse["city"]["sunrise"]
todayWeather["Sunset"] = jsonResponse["city"]["sunset"]
todayWeather["Icon"] = jsonResponse["list"][0]["weather"][0]["icon"]
todayWeather["Str_sunrise"] = str(datetime.fromtimestamp(todayWeather["Sunrise"]))
todayWeather["Str_sunset"] = str(datetime.fromtimestamp(todayWeather["Sunset"]))
# Weather Icon URL : http://openweathermap.org/img/wn/[Icon].png
todayWeather["Icon"] = "http://openweathermap.org/img/wn/" + todayWeather["Icon"] + ".png"

#print( todayWeather )
common.jprint( todayWeather )

# Write json to TodayWeather.json file
fout = open("TodayWeather.json", "w")

# using json.dump to store json format to file
# json.dump() - Takes in a Python object, and converts(dumps) it to a string
json.dump(todayWeather, fout, sort_keys=True, indent=2 )

fout.close()