import turtle
import requests

url = "https://api.wheretheiss.at/v1/satellites/25544"

r = requests.get(url)
data = r.json()
print(data)

latitude = data['latitude']
longitude = data['longitude']
print(latitude)
print(longitude)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('images/map.gif')
screen.register_shape('images/iss.gif')
iss = turtle.Turtle()
iss.shape('images/iss.gif')
iss.setheading(90)
iss.penup()
iss.goto(longitude, latitude)
screen.mainloop()   