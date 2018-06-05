import requests
from functions import *

class Darksky(object):
    darksky_url = 'https://api.darksky.net/forecast/'

    def __init__(self, api_key=None, latitude=None, longitude=None, **kwargs):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.data = None
        self.time = None
        if api_key:
            self._get_darksky_data()

    def _get_darksky_data(self):
        url = Darksky.darksky_url + str(self.api_key) + '/' + str(self.latitude) + ',' + str(self.longitude)
        self.data = requests.get(url).json()
        self.time = datetime.datetime.now()
        replace_in_dict(self.data, search_key='time', replace_func=unixtime_to_readable)

    def _get_hourly_forecast(self):
        return self.data['hourly']['data']

    def _get_minutely_forecast(self):
        return self.data['minutely']['data']

    def _get_current_weather(self):
        return self.data['currently']

    def print_hourly_forecast(self):
        hourly_data = self._get_hourly_forecast()
 
        print('time', 'temperature')
        for data in hourly_data:
            print(data['time'])