# First Sight
- Caching by taking screenshot with using Selenium
- Flag stored in png format

Solution almost clear even with these facts.

- /api/cache takes an url in JSON format.
  for example: 
  ```
  {"url":"https://github.com/abdulmeLINK"}
  ```
- /flag route has white list filter that only grants 127.0.0.1

- gethostbyname(URL) method checks DNS responsed endpoint so it is clear that we can redirect somehow.

# Some of the Possible Solution Scenerios
- Redirecting using your own domain with creating redirector script with few lines of code.
- Using url shortener. (Preffered)

[Python Code](http://github.com/abdulmeLINK/CTFF/HTB/Challenges/baby_CachedView/trick.py)
