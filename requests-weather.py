import requests
import config
import datetime

DARKSKY_FORECAST_URL = 'https://api.darksky.net/forecast/'

header = {'token': config.api_key_darksky}

def get_darksky_data(api_key, lat, long):
    url = DARKSKY_FORECAST_URL + str(header['token']) + '/' + str(lat) + '/' + str(long)
    print(url)
    r = requests.get(DARKSKY_FORECAST_URL + str(header['token']) + '/' + str(lat) + '/' + str(long))

    return r.json()

def show_hourly_forecast(api_key, lat, long):
    response_data = get_darksky_data(api_key, lat, long)
    hourly_forecast = dict()
    hourly_data = response_data['hourly']['data']

    for data in hourly_data:
        hourly_forecast[datetime.datetime.fromtimestamp(data['time']).strftime('%Y-%m-%d %H:%M:%S')] = data['temperature']

    return hourly_forecast

def show_minutely_forecast(api_key, lat, long):
    response_data = get_darksky_data(api_key, lat, long)
    minutely_forecast = dict()
    minutely_data = response_data['minutely']['data']

    for data in mintely_data:
        minutely_forecast[datetime.datetime.fromtimestamp(data['time']).strftime('%Y-%m-%d %H:%M:%S')] = data['temperature']

    return minutely_forecast

print(show_hourly_forecast(header['token'], +35.53860, -97.90141))