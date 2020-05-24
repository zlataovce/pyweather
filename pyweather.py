import requests
from bs4 import BeautifulSoup

url = 'https://weather.com/cs-CZ/pocasi/dnes/l/363d23dbd8c6451caca6c0ef93697c2aa8a47d574bd5b8f4ffbc15360a654d15'
r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
soup = BeautifulSoup(r.content, "html.parser")
temp = soup.find("div", {"class": "today_nowcard-temp"})
phrase = soup.find("div", {"class": "today_nowcard-phrase"})

temperaturestr = temp.text
conditionstr = phrase.text
weatherstr = temperaturestr + " " + conditionstr
