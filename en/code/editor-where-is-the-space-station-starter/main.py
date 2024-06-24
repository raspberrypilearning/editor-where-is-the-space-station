import json
import turtle
import urllib.request

url = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"

response = urllib.request.urlopen(url)
astros = json.loads(response.read())
print(astros)