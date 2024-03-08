import requests

url = "http://localhost:5000/square"

data = {
  "side": 3
}

response = requests.post(url, json=data)

print(response.text)