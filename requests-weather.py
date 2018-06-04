import requests
import config
import datetime

DARKSKY_FORECAST_URL = 'https://api.darksky.net/forecast/'

api_key_darksky = config.api_key_darksky

def get_darksky_data(api_key, lat, long):
    url = DARKSKY_FORECAST_URL + str(api_key) + '/' + str(lat) + ',' + str(long)
    r = requests.get(url)

    return r.json()

def get_hourly_forecast(darksky_data):
    return darksky_data['hourly']['data']


def get_minutely_forecast(darksky_data):
    return darksky_data['minutely']['data']


def get_current_weather(darksky_data):
    return darksky_data['currently']


if __name__=='__main__':
    lat = +35.53860
    long = -97.90141
    darksky_data = get_darksky_data(api_key_darksky, lat, long)
    print(get_minutely_forecast(darksky_data))