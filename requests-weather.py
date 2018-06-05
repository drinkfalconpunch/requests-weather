import requests
import config
import datetime

api_key_darksky = config.api_key_darksky

def unixtime_to_readable(unixtime):
    return datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')

def iterate_dict(src, search_key=None, replace_func=None):
    if isinstance(src, dict):
        for key, value in src.items():
            if key==search_key and replace_func:
                src[key] = replace_func(value)
            else:
                iterate_dict(value, search_key=search_key, replace_func=replace_func)
    elif isinstance(src, list):
        for data in src:
            iterate_dict(data, search_key=search_key, replace_func=replace_func)
    else:
        return src

class Darksky(object):
    darksky_url = 'https://api.darksky.net/forecast/'

    def __init__(self, api_key=None, latitude=None, longitude=None, **kwargs):
        self.api_key = api_key
        self.latitude = latitude
        self.longitude = longitude
        self.data = None
        self.time = None
        if api_key:
            self.get_darksky_data()
        print(self.data)


    def get_darksky_data(self):
        url = Darksky.darksky_url + str(self.api_key) + '/' + str(self.latitude) + ',' + str(self.longitude)
        self.data = requests.get(url).json()
        self.time = datetime.datetime.now()
        self.data = iterate_dict(self.data, search_key='time', replace_func=unixtime_to_readable)


    def get_hourly_forecast(self):
        hourly_data = self.data['hourly']['data']
#        for data in hourly_data:
#            data['time'] = unixtime_to_readable(data['time'])

        return hourly_data

    def get_minutely_forecast(self):
        minutely_data = self.data['minutely']['data']

        for data in minutely_data:
            data['time'] = unixtime_to_readable(data['time']) 

        return minutely_data

    def get_current_weather(self):
        return self.data['currently']

if __name__=='__main__':
    latitude = +35.53860
    longitude = -97.90141
    darksky_data = Darksky(api_key_darksky, latitude, longitude)
    print(darksky_data.get_hourly_forecast())