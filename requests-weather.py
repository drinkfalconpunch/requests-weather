import requests
import config

header = {token: config.api_key}

r = requests.get('https://query.yahooapis.com/v1/public/yql?')
print(r.url)
