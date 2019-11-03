
fin = open("TodayWeather.json", "r")

output = fin.read()

#print(type(output))

today = eval(output)

print(today)
print(today["Description"])
print(today["Temp_min"])
print(today["Temp_max"])
print(today["Sunrise"])
#print(type(today))