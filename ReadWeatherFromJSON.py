# import requests
import json

#todayWeather = ""

f = open("TodayWeather.json", "r")
todayWeather = f.read()

# todayWeather = '{"Wind_speed": 4.03, "Temp_max": 27.18, "Humidity": 44, "Sunset": 1572339014, "Temp_min": 21.92, "Sunrise": 1572290244}'

jsonFormat = json.loads(todayWeather)
weather = eval(todayWeather)

#print(jsonFormat['Temp_max'])
#print(jsonFormat)
#print(weather)

f.close()
