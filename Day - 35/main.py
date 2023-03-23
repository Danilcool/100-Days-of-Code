import requests
import datetime
key = "13074f0cbeff6b6c130934aa89ee85d6"

lon = "103.8519072"
lat = "1.2899175"

result = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}")
data = result.json()
today_wather = data['weather'][0]['main']
time_now = datetime.datetime.now()

print(f'{time_now} {today_wather}')