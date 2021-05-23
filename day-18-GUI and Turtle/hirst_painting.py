"""
import colorgram #used for colors list extraction below

rgb_colors = []
colors = colorgram.extract('hirst_image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

print(rgb_colors)
"""

from turtle import Turtle, Screen
import random

#init the turtle object
timmy = Turtle()
timmy.hideturtle()
timmy.penup()

#init the screen
screen = Screen()
screen.colormode(255)

colors = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

#10x10 -> 100 dots total 
#20 in size spaced 50 apart
timmy.setx(-250)
timmy.sety(-250)
for _ in range(10):
    for _ in range(10):
        timmy.dot(20, random.choice(colors))
        timmy.forward(50)
    direction = timmy.heading()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(direction - 180)
    timmy.forward(50)

screen.exitonclick()