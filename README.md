# pyweather
Python 3 bindings for the weather.com website (scraper)

[![Build Status](https://travis-ci.com/zlataovce/pyweather.svg?branch=master)](https://travis-ci.com/zlataovce/pyweather)

# Supports:
- today & tomorrow temperature and weather phrase
- fahrenheit and celsius

# Dependencies:
- BeautifulSoup4 (pip install BeautifulSoup4)

The scraper needs the url of a city/town weather overview (page when you click on a city/town) and a string passed to the temp function for the unit (f for fahrenheit and c for celsius). 

# Example code:
import pyweather

print(pyweather.today.temp("https://weather.com/weather/today/l/f892433d7660da170347398eb"
                           "8e3d722d8d362fe7dd15af16ce88324e1b96e70", "c"))


This prints the current temperature in New York in Celsius.
