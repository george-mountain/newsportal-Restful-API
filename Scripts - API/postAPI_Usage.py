import requests
from decouple import config


""" POSTING to the API ENDPOINT using request package"""

API_KEY = config("API_KEY")
base_url = "http://127.0.0.1:8000/api/v1/"

title = "Testing Post using Request"
body = "This test is for request after configuring API usage"
author = "testuser1"
image_path = "C:/Users/george ugwu/Downloads/AI and Explainable AI (XAI) Trends in Healthcare (2).jpg"

url = base_url

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
    response = requests.post(url, headers=headers, data=data, files=files)

    print(response.status_code)
    print(response.json())
except Exception as e:
    print(e)
