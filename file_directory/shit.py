import random
import string
import requests


key = "".join(random.choices(string.ascii_letters + string.digits, k=30))
weather_api = requests.get(
    f"http://api.weatherapi.com/v1/current.json?key={key}&q=auto:ip"
)
while True:
    if weather_api.status_code == 200:
        print(key)
    else:
        key = "".join(random.choices(string.ascii_letters + string.digits, k=30))
        weather_api = requests.get(
            f"http://api.weatherapi.com/v1/current.json?key={key}&q=auto:ip"
        )
