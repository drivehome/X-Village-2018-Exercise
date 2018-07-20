import requests
import json

response = requests.get('https://www.metaweather.com/api/location/2306179/2018/7/18')

highest_predictability = 0
predictability_weather_state = "None"

with open('Taipei_weather.json', 'r', encoding='utf-8-sig') as f:
    Taipei_weather = json.load(f)
    for row in Taipei_weather:
        if highest_predictability < row["predictability"]:
            highest_predictability = row["predictability"]
            predictability_weather_state = row["weather_state_name"]

print("Taipei's weather is {}".format(predictability_weather_state))