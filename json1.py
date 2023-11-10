import requests
import json


response = requests.get("https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign=capricorn&day=today")
data = response.json()  


with open("horoscope_data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Data stored successfully!")