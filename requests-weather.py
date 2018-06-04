import requests
import config
import datetime

DARKSKY_FORECAST_URL = 'https://api.darksky.net/forecast/'

api_key_darksky = config.api_key_darksky

def get_darksky_data(api_key, lat, long):
    url = DARKSKY_FORECAST_URL + str(api_key) + '/' + str(lat) + ',' + str(long)
    r = requests.get(url)

    return r.json()

def get_hourly_forecast(api_key, lat, long):
    response_data = get_darksky_data(api_key, lat, long)
    hourly_forecast = dict()
    hourly_data = response_data['hourly']['data']

#    for data in hourly_data:
#        hourly_forecast[datetime.datetime.fromtimestamp(data['time']).strftime('%Y-%m-%d %H:%M:%S')] = data['temperature']

    return hourly_data

def get_minutely_forecast(api_key, lat, long):
    response_data = get_darksky_data(api_key, lat, long)
    minutely_forecast = dict()
    minutely_data = response_data['minutely']['data']

#    for data in minutely_data:
#        minutely_forecast[datetime.datetime.fromtimestamp(data['time']).strftime('%Y-%m-%d %H:%M:%S')] = data['temperature']

    return minutely_data

def get_current_weather(api_key, lat, long):
    response_data = get_darksky_data(api_key, lat, long)
    current_weather = response_data['currently']

    return current_weather


if __name__=='__main__':
    print(get_minutely_forecast(api_key_darksky, +35.53860, -97.90141))