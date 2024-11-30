import requests

IP_INFO_URL = "http://ipinfo.io"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = ""

def get_current_weather():
    location_response = requests.get(IP_INFO_URL).json()
    city = location_response['city']
    country = location_response['country']
    weather_response = requests.get(WEATHER_URL, params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }).json()
    print(weather_response)
    return {
        "city": city,
        "country": country,
        "degrees": weather_response['main']['temp']
    }


def get_city_weather(city):
    weather_response = requests.get(WEATHER_URL, params={
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }).json()
    
    return {
        "city": weather_response['name'],
        "country": weather_response['sys']['country'],
        "degrees": weather_response['main']['temp']
    }

