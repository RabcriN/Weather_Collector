import os
import sqlite3
from sqlite3 import Error

from constants import BASE_DIR


def create_connection(path=BASE_DIR, name: str = 'weather_db.sqlite'):
    connection = None
    try:
        connection = sqlite3.connect(os.path.join(path, name))
        print('Connection to SQLite DB successful')
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")


create_cities_table = """
CREATE TABLE IF NOT EXISTS cities (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  temperature INTEGER,
  temperature_min INTEGER,
  temperature_max INTEGER,
  weather_type TEXT,
  city_name TEXT,
  feels_like INTEGER,
  country TEXT,
  current_city_time TEXT
);
"""


def create_city(city):
    return (f"""
      INSERT INTO
      cities (temperature, temperature_min, temperature_max, weather_type,
      city_name, feels_like, country, current_city_time)
      VALUES
      {city}
    """)


def write_to_db(connection, city):
    city = (
        city.temperature,
        city.temperature_min,
        city.temperature_max,
        city.weather_type.value,
        city.city_name,
        city.feels_like,
        city.country,
        city.current_city_time.strftime('%D %H:%M')
    )
    execute_query(connection, create_city(city))
