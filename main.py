# Start to my IMDB Project
import requests
import json
import imdb
import psec
import requests

url = "https://imdb-api.com/en/API/Top250TVs/k_hwmq4lj0"
payload = {}
headers = {}
response_API = requests.request("GET", url, headers=headers, data=payload)
# print(response_API.status_code)
data = response_API.text
json.loads(data)
parse_json = json.loads(data)
print(data)
# info = parse_json['items'][0]['rank']
# test = []
print((parse_json['items'][0]['rank']))
