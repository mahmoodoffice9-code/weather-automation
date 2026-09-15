import datetime
import requests

city = 'Bahawalpur'
url = f'https://wttr.in/{city}?format=j1'

# Baghair try-except ke taake error khul kar samne aaye
response = requests.get(url)
print('Response Status:', response.status_code)

data = response.json()
current = data['current_condition'][0]
temp = current['temp_C']
humidity = current['humidity']
condition = current['weatherDesc'][0]['value']

timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
log = (
    f'[{timestamp}] City: {city} | Temp: {temp}C | Humidity: {humidity}% |'
    f' Condition: {condition}\n'
)

print(log)

# File save karna
with open('weather_log.txt', 'w') as f:
  f.write(log)

print('File successfully created and saved!')
