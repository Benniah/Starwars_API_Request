import requests
import pandas as pd
import json

baseurl = 'https://swapi.dev/api/'
endpoint = 'planets/'


def remove_unknown(data):
    data = data
    if data == 'unknown':
        data = data.replace('unknown', '0')
    elif data == '[]':
        data = data.replace('[]', '0')

    else:
        return data


def convert_list_to_string(data):
    if len(data):
        return f"{data}"


def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()


def parse_json(response):
    starwars = []
    for item in response['results']:
        stars = {

         'planet_name': item['name'],
         'rotation_period': item['rotation_period'],
         'orbital_period': item['orbital_period'],
         'diameter': item['diameter'],
         'climate': item['climate'],
         'gravity': item['gravity'],
         'terrain': item['terrain'],
         'surface_water': remove_unknown(item['surface_water']),
         'population': remove_unknown(item['population']),
         'residents': convert_list_to_string(item['residents']),
         'films': convert_list_to_string(item['films']),
         'created': item['created'],
         'edited': item['edited'],
         'url': item['url']

        }
        starwars.append(stars)
    return starwars


mainlist = []
for x in range(1, 7):
    mainlist.extend(parse_json(main_request(baseurl, endpoint, x)))


print(mainlist)
