import requests
import json

locations = ['Chicago, IL', 'San Francisco, CA']

city_data_url = 'http://api.sba.gov/geodata/primary_links_for_city_of/%s/%s.json'

for l in locations:
    split_name = l.split(', ')
    response = requests.get(city_data_url % tuple(split_name))
    
    print(response.text)  # Add this line to check the response content
    resp_json = json.loads(response.text)


    resp_json = json.loads(response.text)
    print(resp_json[0]['full_county_name'])