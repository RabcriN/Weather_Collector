import json
from datetime import datetime, timedelta
from enum import Enum
from json.decoder import JSONDecodeError
from typing import NamedTuple

import requests

from constants import OPEN_WEATHER_URL_BY_CITY
from exceptions import ApiServiceError

Celsius = int


class WeatherType(Enum):
    THUNDERSTORM = 'THUNDERSTORM'
    DRIZZLE = 'DRIZZLE'
    RAIN = 'RAIN'
    SNOW = 'SNOW'
    CLEAR = 'CLEAR'
    FOG = 'FOG'
    CLOUDS = 'CLOUDS'


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    city_name: str
    feels_like: Celsius
    temperature_min: Celsius
    temperature_max: Celsius
    country: str
    current_city_time: datetime


def get_weather_in_city(city: str) -> Weather:
    """Requests weather from openweather API and returns it"""
    openweather_response = _get_openweather_response_in_city(city)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _get_openweather_response_in_city(city: str) -> bytes:
    """Requests weather in city and returns it"""
    url = OPEN_WEATHER_URL_BY_CITY.format(city=city)
    if requests.get(url).status_code == 404:
        errmsg = f"Can't find weather in city '{city}'"
        raise ApiServiceError(errmsg)
    try:
        return requests.get(url).content
    except Exception:
        raise ApiServiceError


def _parse_openweather_response(openweather_response: bytes) -> Weather:
    """Parse weather response data and returns Weather"""
    try:
        openweather_dict = json.loads(openweather_response)
    except JSONDecodeError:
        raise ApiServiceError
    return Weather(
        temperature=_parse_temperatures(openweather_dict),
        temperature_min=_parse_min_temperatures(openweather_dict),
        temperature_max=_parse_max_temperatures(openweather_dict),
        weather_type=_parse_weather_type(openweather_dict),
        city_name=_parse_location(openweather_dict),
        feels_like=_parse_feels_like(openweather_dict),
        country=_parse_country(openweather_dict),
        current_city_time=_parse_current_time(openweather_dict),
    )


def _parse_temperatures(openweather_dict: dict) -> Celsius:
    return round(openweather_dict['main']['temp'])


def _parse_feels_like(openweather_dict: dict) -> Celsius:
    return round(openweather_dict['main']['feels_like'])


def _parse_min_temperatures(openweather_dict: dict) -> Celsius:
    temp_min = round(openweather_dict['main']['temp_min'])
    return temp_min


def _parse_max_temperatures(openweather_dict: dict) -> Celsius:
    temp_max = round(openweather_dict['main']['temp_max'])
    return temp_max


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict['weather'][0]['id'])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        '2': WeatherType.THUNDERSTORM,
        '3': WeatherType.DRIZZLE,
        '5': WeatherType.RAIN,
        '6': WeatherType.SNOW,
        '7': WeatherType.FOG,
        '800': WeatherType.CLEAR,
        '80': WeatherType.CLOUDS,
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    errmsg = f"Can't parse weather_type {weather_type_id}'"
    raise ApiServiceError(errmsg)


def _parse_location(openweather_dict: dict) -> str:
    try:
        return openweather_dict['name']
    except (KeyError):
        raise ApiServiceError


def _parse_country(openweather_dict: dict) -> str:
    try:
        return openweather_dict['sys']['country']
    except (KeyError):
        raise ApiServiceError


def _parse_current_time(openweather_dict: dict) -> datetime:
    try:
        city_time_zone = openweather_dict['timezone']
    except (KeyError):
        raise ApiServiceError
    current_time_zone = (
        datetime.utcnow().astimezone()
        .utcoffset().total_seconds()  # type:ignore
    )
    time = datetime.now() + timedelta(
        seconds=city_time_zone - current_time_zone
    )
    return time
