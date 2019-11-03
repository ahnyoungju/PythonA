# Get Weather Data From Openweathermap

import requests
import json

url = "http://api.openweathermap.org/data/2.5/forecast?q=Melbourne,AU&units=metric&APPID=e79c59d54b437abefcab039dd2657f5c"

response = requests.get(url)

#print(response.text[:1000])
#print( type(response.text))

todayWeather = {}

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


sunrise = jsonFormat["city"]["sunrise"]
timezone = jsonFormat["city"]["timezone"]
sunset = jsonFormat["city"]["sunset"]
print( todayWeather )

# Write json to TodayWeather.json file
fout = open("TodayWeather.json", "w")
#fout.write(str(todayWeather))

# using json.dump to store json format to file
json.dump(todayWeather, fout)

fout.close()
