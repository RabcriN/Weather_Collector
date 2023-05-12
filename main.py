import time

from tqdm import tqdm

from cities import parse_city_names
from db import (create_cities_table, create_connection, execute_query,
                write_to_db)
from weather_api_service import get_weather_in_city


def main():
    db_connection = create_connection()
    execute_query(db_connection, create_cities_table)
    city_list = parse_city_names()
    for city in tqdm(city_list, desc='Collecting data and writing into DB'):
        write_to_db(db_connection, get_weather_in_city(city))
    db_connection.close()
    print("Job's done. Next start in an hour.")


if __name__ == "__main__":
    while True:
        main()
        time.sleep(3600)
