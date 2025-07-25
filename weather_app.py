import requests
import json
import os

API_KEY = os.environ.get("OPENWEATHER_API_KEY")
if not API_KEY:
    print("Error: OpenWeatherMap API key not found.")
    print("Please set the 'OPENWEATHER_API_KEY' environment variable.")
    exit() 

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter the city name: ")

request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"

print(f"Fetching weather for {city}:....")
response = requests.get(request_url)

if response.status_code == 200:
    print(" Succeful Request! Processing data....")
    data = response.json()
    weather_description = data['weather'][0]['description']
    temperature_kelvin = data['main']['temp']
    city_name_from_api = data['name']
    temperature_celsius = temperature_kelvin - 273.15
    temprature_fahrenheit = temperature_celsius * 9/5 + 32
    print(f"\nWeather in {city_name_from_api}:")
    print(f"  Description: {weather_description.capitalize()}")
    print(f"  Temperature: {temperature_celsius:.2f}°C / {temprature_fahrenheit:.2f}°F")
else:
    print(f"Error fetching data: HTTP Status Code {response.status_code}")