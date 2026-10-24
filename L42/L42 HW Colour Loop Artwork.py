import turtle

screen = turtle.Screen()
screen.bgcolor("black")

artist = turtle.Turtle()
artist.speed(0)
artist.width(2)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(120):
    artist.pencolor(colors[i % len(colors)])
    artist.forward(i * 3)
    artist.left(59)

turtle.done()