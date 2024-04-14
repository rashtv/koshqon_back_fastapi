from typing import List

from api.databases.db_client import cities_collection


def city_helper(city) -> dict:
    return {
        'id': city['_id'],
        'code': city['code'],
        'name': city['name'],
        'country': city['country'],
    }


async def retrieve_cities() -> List:
    cities = []
    async for city in cities_collection.find():
        cities.append(city_helper(city))
    return cities
