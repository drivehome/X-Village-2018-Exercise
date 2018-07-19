import json 
import requests
 
url = 'https://www.metaweather.com/api/location/2306179/'
r = requests.get(url)
r.encoding = 'utf-8' 
print(r.text)
