import requests
from bs4 import BeautifulSoup


class today:
	def temp(url):
		r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
									   'Intel Mac OS X 10_12_6) AppleWebKit/537.36'
									   '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
		soup = BeautifulSoup(r.content, "html.parser")
		temp = soup.find("div", {"class": "today_nowcard-temp"})
		temperaturestr = temp.text
		return temperaturestr
	
	
	def phrase(url):
		r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
									   'Intel Mac OS X 10_12_6) AppleWebKit/537.36'
									   '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
		soup = BeautifulSoup(r.content, "html.parser")
		phrase = soup.find("div", {"class": "today_nowcard-phrase"})
		phrasestr = phrase.text
		return phrasestr
