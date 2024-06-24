import turtle
import requests

url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"

r = requests.get(url)
data = r.json()
print(data)