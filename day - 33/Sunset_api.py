import requests
import datetime

my_lat = 1.352083
my_long = 103.819839
parameters = {
    'lat': my_lat,
    "lng": my_long,
    'formatted':0,
}
response= requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunset)
print(sunrise)

time_now = datetime.datetime.now()

print(time_now.hour)
