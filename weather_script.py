# openweather api로 요청을 해서
# 그 결과로 csv로 저장하는 py


import requests
import csv
from datetime import datetime
import os

CITY = "Seoul"
API_KEY = "9fadb9e4f9dc7a4dd06af1292e205930"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
print(data)
temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
description = data["weather"][0]["description"]
print(temp, humidity, description)
print(datetime.now())
