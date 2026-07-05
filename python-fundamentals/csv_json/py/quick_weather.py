#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: YangFei
@time: 2024/11/11 15:21 
@file: quick_weather.py
@project: ReLearn
@email: ccc420513@gmail.com
"""
import json,sys,requests
APPID='d079d71c83aecd32571d0e21be0d6e16'

if len(sys.argv)<2:
    print("Usage:quick_weather.py location")
    sys.exit()
location=' '.join(sys.argv[1:])

# Download the json data from OpenWeatherMap.org'API
url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={APPID}&units=metric'
response=requests.get(url)
response.raise_for_status()
#load json data into a python value
weather_data=json.loads(response.text)
w=weather_data['list']
#print weather description
print(f'Current weater in {location}')
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print('tomorrow:')
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])



