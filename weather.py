import datetime
import os
import requests

city = 'Bahawalpur'
url = f'https://wttr.in/{city}?format=j1'

try:
  response = requests.get(url)
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

  # Explicit path check
  file_path = os.path.join(os.getcwd(), 'weather_log.txt')
  with open(file_path, 'a') as f:
    f.write(log)
  print(f'Successfully saved to {file_path}')

except Exception as e:
  print(f'Error fetching weather data: {e}')
