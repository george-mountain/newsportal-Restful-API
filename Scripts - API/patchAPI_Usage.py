import requests
from decouple import config

""" 
Patching a resource using the request package
As can be seen below, we don't need to provide
all the fields while using the patch

"""

API_KEY = config("API_KEY")
base_url = "http://127.0.0.1:8000/api/v1/"

resource_id = 7  # Replace with the actual resource ID

url = "{}{}".format(base_url, resource_id)

headers = {
    "Authorization": "Token {}".format(API_KEY),
}

data = {
    "title": "Patching resource test from request -- Modified",
    "author": "nzute",
}

try:
    response = requests.patch(url, headers=headers, data=data)
    print(response.status_code)
    print(response.json())
except Exception as e:
    print(e)
