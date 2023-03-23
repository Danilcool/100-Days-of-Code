import datetime

import requests

MY_LAT = 1.352083 # Your latitude
MY_LONG = 103.819839 # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

current_time = datetime.datetime.now()
current_hour = current_time.hour
print(current_hour)
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


##### check for time

response= requests.get(url='https://api.sunrise-sunset.org/json',params=parameters)
response.raise_for_status()

data = response.json()

sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

print(sunrise,sunset)

if iss_longitude-5 > MY_LONG and iss_latitude + 5 < MY_LONG and iss_latitude - 5 > MY_LAT and iss_latitude+5 < MY_LONG:
    pass



#Your position is within +5 or -5 degrees of the ISS position.


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



