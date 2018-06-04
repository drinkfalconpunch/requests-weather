import requests
import config
import datetime

api_key_darksky = config.api_key_darksky

def unixtime_to_readable(unixtime):
    return datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')

class Darksky(object):
    DARKSKY_FORECAST_URL = 'https://api.darksky.net/forecast/'

    def __init__(self, api_key=None, lat=None, long=None, **kwargs):
        self.api_key = api_key
        self.lat = lat
        self.long = long
        self.data = None
        self.time = None
        if api_key is not None:
            self.get_darksky_data()


    def get_darksky_data(self):
        url = Darksky.DARKSKY_FORECAST_URL + str(self.api_key) + '/' + str(self.lat) + ',' + str(self.long)
        self.data = requests.get(url).json()
#        for key, value in dictionary.items():
#            if isinstance(value, dict):
#                iterate(value)
#                continue
        self.time = datetime.datetime.now()


    def get_hourly_forecast(self):
        hourly_data = self.data['hourly']['data']
        for data in hourly_data:
            data['time'] = unixtime_to_readable(data['time'])

        return hourly_data

    def get_minutely_forecast(self):
        minutely_data = self.data['minutely']['data']

        for data in minutely_data:
            data['time'] = unixtime_to_readable(data['time']) 

        return minutely_data

    def get_current_weather(self):
        current_weather = self.data['currently']

        return current_weather

if __name__=='__main__':
    lat = +35.53860
    long = -97.90141
    darksky_data = Darksky(api_key_darksky, lat, long)
    print(darksky_data.get_current_weather())