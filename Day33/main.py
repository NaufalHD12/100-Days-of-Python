import requests
import datetime
# HTTP CODES
# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up

MY_LAT = -6.352798
MY_LNG = 108.324341
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

MY_LAT = -6.352798
MY_LNG = 108.324341

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(data["results"]["sunrise"])
print(data["results"]["sunset"])
print(sunrise)
print(sunset)

time_now = datetime.datetime.now()
print(time_now.hour)