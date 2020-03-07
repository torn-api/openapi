#!/usr/bin/env python
import paths
import requests
import os
import yaml
from dotenv import load_dotenv
load_dotenv()



api_key = os.getenv('TORN_API_KEY')

if api_key is None:
    print('Please set your API-Key as Environment Variable.')
    exit(1)


def fetch(path, params):
    url = f'https://api.torn.com{path}'
    params['key'] = api_key
    response = requests.get(url, params)
    return response.json()

f = open("user-example.yaml", "w")
for param in paths.user:
    data = fetch('/user', {'selections': param})
    data = { param: data }
    f.write(yaml.dump(data))
    f.write("\n")
f.close()

