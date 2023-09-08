# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
turtle.Screen().bgcolor('black')
for x in range(360):
    turtle.pencolor(colors[x%6])
    turtle.width(x//100 + 1)
    turtle.forward(x)
    turtle.left(59)