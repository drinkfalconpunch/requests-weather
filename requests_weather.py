import requests
from datetime import datetime
from config import Config
from utils import unixtime_to_readable, replace_in_dict

DARKSKY_URL = "https://api.darksky.net/forecast/"


class Darksky(object):
    def __init__(self, **kwargs):
        self.latitude = None
        self.longitude = None
        self.data = None
        self.time = None

    def get_darksky_data(self):
        url = (
            DARKSKY_URL
            + str(Config.DARKSKY_API_KEY)
            + "/"
            + str(self.latitude)
            + ","
            + str(self.longitude)
        )
        self.data = requests.get(url).json()
        self.time = datetime.now()
        replace_in_dict(self.data, search_key="time", replace_func=unixtime_to_readable)

    def get_hourly_forecast(self):
        return self.data["hourly"]["data"]

    def get_minutely_forecast(self):
        return self.data["minutely"]["data"]

    def get_current_weather(self):
        return self.data["currently"]

    def print_hourly_forecast(self):
        hourly_data = self.get_hourly_forecast()

        print("time", "temperature")
        for data in hourly_data:
            print(data["time"])

