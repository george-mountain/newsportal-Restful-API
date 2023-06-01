import requests
import json
from decouple import config


"""Retrieving posts using Request commands"""

API_KEY = config("API_KEY")
base_url = "http://127.0.0.1:8000/api/v1/"

url = base_url

headers = {
    "Authorization": "Token {}".format(API_KEY),
}

try:
    response = requests.get(url, headers=headers)

    print(response.status_code)
    response_json = response.json()
    formatted_json = json.dumps(response_json, indent=4)
    print(formatted_json)
except Exception as e:
    print(e)
