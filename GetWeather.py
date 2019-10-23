# Get Weather Data From Openweathermap

import requests
import json

url = "http://api.openweathermap.org/data/2.5/forecast?q=Melbourne,AU&units=metric&APPID=e79c59d54b437abefcab039dd2657f5c"

response = requests.get(url)

#print(response.text[:1000])
#print( type(response.text))

jsonFormat = json.loads(response.text)
print( jsonFormat["list"][0]["weather"][0]["main"])
print( jsonFormat["list"][0]["weather"][0]["description"])