import requests
import json

locations = ['Chicago, IL', 'San Francisco, CA']

city_data_url = 'http://api.sba.gov/geodata/primary_links_for_city_of/%s/%s.json'

for l in locations:
    split_name = l.split(', ')
    response = requests.get(city_data_url % tuple(split_name))

    resp_json = json.loads(response.text)
    print(resp_json[0]['full_county_name'])