import re
from typing import Any, Literal, Union

import requests

from constants import COUNTRIES_URL
from exceptions import ApiServiceError


def get_city_list(
        limit: int = 50,
        order: Union[Literal['dsc'], Literal['asc']] = 'dsc',
        orderBy: str = 'populationCounts'
        ) -> Any:
    json = {
        'limit': limit,
        'order': order,
        'orderBy': orderBy,
    }
    url = COUNTRIES_URL
    r = requests.post(url, json=json)
    return r.json()


def parse_city_names() -> list[str]:
    cities_list = []
    try:
        data = get_city_list()['data']
    except (KeyError):
        errmsg = "Can't find data in cities list"
        raise ApiServiceError(errmsg)
    for city in data:
        city = re.sub('\\([^()]*\\)', '', city['city'])
        if city == 'HONG KONG SAR':
            city = 'HONG KONG'
        if 'Greater' in city:
            city = city.replace('Greater', '')
        cities_list.append(city)
    return cities_list
