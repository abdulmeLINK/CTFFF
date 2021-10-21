# First Sight
- Caching by taking screenshot with using Selenium
- Flag stored in png format

Solution almost clear even with these facts.

- /api/cache takes an url in JSON format.
  for example: [code]{"url":"https://github.com/abdulmeLINK"}[/code]
  
- /flag route has white list filter that only grants 127.0.0.1

- gethostbyname(URL) method checks DNS responsed endpoint so it is clear that we can redirect somehow.

# Some of the Possible Solution Scenerios
- Redirecting using your own domain with creating redirector script with few lines of code.
- Using url shortener. (Preffered)


