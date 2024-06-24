import requests

url = "https://api.wheretheiss.at/v1/satellites/25544"

r = requests.get(url)
data = r.json()
print(data)