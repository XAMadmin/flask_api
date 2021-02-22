import requests
import json

response = requests.post(url = "http://127.0.0.1:8080/api/v1.0/store_info")

data = json.loads(response.text)

print(data)