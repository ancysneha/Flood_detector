import requests

API_KEY = "your_api_key_here"  # You will add key soon
CITY = "Coimbatore"

def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    weather = {
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "rain": data["weather"][0]["main"] == "Rain"
    }

    return weather
