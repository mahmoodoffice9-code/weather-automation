import datetime
import requests

# City name (Aap apni marzi ka bhi rakh sakte hain)
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

  # Log file mein data save karna
  with open('weather_log.txt', 'a') as f:
    f.write(log)

except Exception as e:
  print(f'Error fetching weather data: {e}')
