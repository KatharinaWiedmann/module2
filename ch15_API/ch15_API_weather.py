# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:34:57 2019

@author: Katharina
"""

#to make this work, items in CAPITALS need to be inserted 

import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "Munich,Germany", "units":"metric", "appid":"APP ID"}

response = requests.get(endpoint, params=payload)
data = response.json()

print(data)

print(response.url)
print(response.status_code)
print(response.headers["content-type"])


temperature = data['main']['temp']
name = data['name']
weather = data['weather'][0]['main']
print('TEMPERATURE', temperature)
print('WEATHER', weather)

print('It is {}C in {}, and the sky is {}'.format(temperature, name, weather))

