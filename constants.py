import os
from secrets import API_KEY

COUNTRIES_URL = (
    'https://countriesnow.space/api/v0.1/countries/'
    'population/cities/filter'
)

OPEN_WEATHER_URL_BY_CITY = (
    'https://api.openweathermap.org/data/2.5/weather?'
    'q={city}&'
    'appid=' + API_KEY + '&lang=en&units=metric'
)

BASE_DIR = dir_path = os.path.dirname(os.path.realpath(__file__))
