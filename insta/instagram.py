import requests
from bs4 import BeautifulSoup

url = 'https://www.instagram.com/'
links = ['kimelya_11']

result = requests.get(url + links[0])
soup = BeautifulSoup(result.text)

scripts = soup.findAll('script', {'type': 'text/javascript'})

print(scripts[3])

with open(links[0] + ".html", "w", encoding="utf-8") as f:
    f.write(result.text)
