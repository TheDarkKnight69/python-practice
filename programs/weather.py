import requests
import ipapi
import time


print("Welcome to Weather Forecast: ")
print(
    """Do you want to :
      (1) Enter your location
      (2) Automatically detect it?   
      
      
      P.S: The automatic method is not very accurate
      """
)
choice = input(">>> ")
if choice != "1":
    location_ = ipapi.location()
else:
    print("Enter your location")
    location_ = input(">>> ")
key = "ae41bbfd8cfd438eae863240230206"
weather_api = requests.get(
    f"http://api.weatherapi.com/v1/current.json?key={key}&q={location_}"
)
global w, t, p
w = weather_api.json()
t = w["location"]
p = w["current"]


def weather_details():
    print("\n")
    print("\n")
    print("\n")
    print("\n")
    print("Welcome to Weather Forecast")
    print(f'Displaying Forecast for {t["name"]}')
    print(f'Country:   {t["country"]}')
    print(f'Latitude:  {t["lat"]}\u00B0   |      Longitude:      {t["lon"]}\u00B0')
    print(f'Local Time:      {t["localtime"]}')
    print("========================")
    print("Weather Conditions: ")
    print("Temperature: ")
    print(
        f'Celsius:       {p["temp_c"]}\u00B0C   |   Farenheit:    {p["temp_f"]}\u00B0F'
    )
    print("=========================")
    print("Wind Details: ")
    print(f'Wind Speed:    {p["wind_mph"]}mph')
    print(f'Wind Direction:       {p["wind_dir"]}')
    print("==========================")
    print("Others: ")
    print(f'Precipitation [mm]:        {p["precip_mm"]}mm')
    print(f'Humidity:      {p["humidity"]}%')
    print(f'Feels like:       {p["feelslike_c"]}\u00B0C or {p["feelslike_f"]}\u00B0F')
    print(f'Visibility:     {p["vis_km"]} km or {p["vis_miles"]} miles')
    print("==========================")
    print("\n")
    print("\n")
    print("\n")
    print(f'Last updated at:        {p["last_updated"]}')


weather_message = """
Choose an option:
(1) Weather Details
(2)....
"""
print(weather_message)
weather_confirmation = input(">>> ")
if weather_confirmation == "1":
    print("Okay. Loading...")
    time.sleep(2)
    weather_details()
    time.sleep(5)
    print(weather_message)
else:
    print("foo")
