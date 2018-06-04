import requests
import config
import datetime

api_key_darksky = config.api_key_darksky

def unixtime_to_readable(unixtime):
    return datetime.datetime.fromtimestamp(unixtime).strftime('%Y-%m-%d %H:%M:%S')

def iterate_dict(src, search_key=None, replace_func=None, in_place=False):
    if isinstance(src, dict):
        for key, value in src.items():
            if key==search_key and replace_func:
                value = replace_func(value)
            else:
                value = iterate_dict(value, search_key=search_key, replace_func=replace_func)
    elif isinstance(src, list):
        for data in src:
            data = iterate_dict(data, search_key=search_key, replace_func=replace_func)
    else:
        print(src)

class Darksky(object):
    darksky_url = 'https://api.darksky.net/forecast/'

    def __init__(self, api_key=None, lat=None, long=None, **kwargs):
        self.api_key = api_key
        self.lat = lat
        self.long = long
        self.data = None
        self.time = None
        if api_key is not None:
            self.get_darksky_data()
        print(self.data)


    def get_darksky_data(self):
        url = Darksky.darksky_url + str(self.api_key) + '/' + str(self.lat) + ',' + str(self.long)
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
    lat = +35.53860
    long = -97.90141
    darksky_data = Darksky(api_key_darksky, lat, long)
    print(darksky_data.get_hourly_forecast())