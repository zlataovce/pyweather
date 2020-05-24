import requests
from bs4 import BeautifulSoup


class today:
    def temp(url, tmp):
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
                                       'Intel Mac OS X 10_12_6) AppleWebKit/53'
                                       '7.36(KHTML, like Gecko) Chrome/63.0.32'
                                       '39.132 Safari/537.36'})
        soup = BeautifulSoup(r.content, "html.parser")
        temp = soup.find("div", {"class": "today_nowcard-temp"})
        temperaturestr = str(temp.text)
        if tmp == "c":
            withoutdegree = temperaturestr.replace("°", "")
            temperaturewithoutdgr = (withoutdegree - 32) * 5.0/9.0
            temperature = str(temperaturewithoutdgr) + "°"
            return temperature
        else:
            return temperaturestr

    def phrase(url):
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
                                       'Intel Mac OS X 10_12_6) AppleWebKit/53'
                                       '7.36(KHTML, like Gecko) Chrome/63.0.32'
                                       '39.132 Safari/537.36'})
        soup = BeautifulSoup(r.content, "html.parser")
        phrase = soup.find("div", {"class": "today_nowcard-phrase"})
        phrasestr = phrase.text
        return phrasestr


class tomorrow:
    def temp(url):
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
                                       'Intel Mac OS X 10_12_6) AppleWebKit/53'
                                       '7.36(KHTML, like Gecko) Chrome/63.0.32'
                                       '39.132 Safari/537.36'})
        soup = BeautifulSoup(r.content, "html.parser")
        daypart = soup.find("div", {"id": "daypart-1"})
        temp = daypart.find("div", {"class": "today-daypart-temp"})
        temperaturestr = str(temp.text)
        if tmp == "c":
            withoutdegree = temperaturestr.replace("°", "")
            temperaturewithoutdgr = (withoutdegree - 32) * 5.0/9.0
            temperature = str(temperaturewithoutdgr) + "°"
            return temperature
        else:
            return temperaturestr

    def phrase(url):
        r = requests.get(url, headers={'user-agent': 'Mozilla/5.0 (Macintosh; '
                                       'Intel Mac OS X 10_12_6) AppleWebKit/53'
                                       '7.36(KHTML, like Gecko) Chrome/63.0.32'
                                       '39.132 Safari/537.36'})
        soup = BeautifulSoup(r.content, "html.parser")
        daypart = soup.find("div", {"id": "daypart-1", "class": "today-daypart"
                                    "daypart-1 selected"})
        phrase = daypart.find("span", {"id": "dp1-phrase"})
        phrasestr = phrase.text
        return phrasestr
