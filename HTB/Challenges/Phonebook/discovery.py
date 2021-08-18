import requests
import string
s = requests.session()
url = '__URL__'

printables = string.printable
for pr in printables:
    data = {
        "username": pr,
        "password": pr
    }
    r = s.post(url, data=data)
    if 'username' not in r.text and 'passowrd' not in r.text:
        print(r.text)
        print('char of interest:', pr)
