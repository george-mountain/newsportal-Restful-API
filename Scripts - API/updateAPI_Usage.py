import requests
from decouple import config


"""Updating POST from the API endpoint using PUT"""

API_KEY = config("API_KEY")
base_url = "http://127.0.0.1:8000/api/v1/"

title = "Modified Post test using request package"
body = "ModifiedTesting the API end point from the python file using request package"
author = "testuser1"
image_path = "C:/Users/george ugwu/Downloads/ml2.png"
post_id = 7

url = "{}{}/".format(base_url, post_id)

headers = {
    "Authorization": "Token {}".format(API_KEY),
}

data = {
    "title": title,
    "body": body,
    "author": author,
}

files = {
    "image": open(image_path, "rb"),
}

try:
    response = requests.put(url, headers=headers, data=data, files=files)

    print(response.status_code)
    print(response.json())
except Exception as e:
    print(e)
