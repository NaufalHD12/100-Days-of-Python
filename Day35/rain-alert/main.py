import requests
import smtplib

my_email = "hadinaufal06@gmail.com"
app_password = "wagt rwwt hsqf jjrr"  # Gunakan App Password dari Google

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "cc284d8e719e355ca215ab2b2667aac3"

parameters = {
    "lat": -6.352798,
    "lon": 108.324341,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = any(int(entry["weather"][0]["id"]) < 700 for entry in data["list"])

if will_rain:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=app_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="naufalhd4@gmail.com",
            msg="Subject:Weather Alert\n\nIt's going to rain today. Remember to bring an umbrella."
        )

    print("Email sent successfully!")
