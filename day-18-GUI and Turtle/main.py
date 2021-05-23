#import turtle
#import turtle as t
#from turtle import *

from turtle import Turtle, Screen
import random
#init the turtle object
timmy = Turtle()
timmy.shape("turtle")
timmy.color("light blue")
#init the screen
screen = Screen()
screen.colormode(255)

#18.1 Coding Challenge - draw a square
for _ in range(4):
  timmy.forward(100)
  timmy.right(90)

#18.2 Coding Challenge - draw a dashed line
for _ in range(25):
  timmy.pendown()
  timmy.forward(5)
  timmy.penup()
  timmy.forward(5)

#18.3 Coding Challenge - drawing shapes
#triangle,square, pentagon,...decagon (3,4,5...10 sides)
def draw_shape(num_sides):
  deg = 360 / num_sides
  for _ in range(num_sides):
    timmy.forward(100)
    timmy.right(deg)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

for sides in range(3,11):
  timmy.color(random.choice(colors))
  draw_shape(sides)

#18.4 Coding Challenge - random walk
#speed up, thicker line
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy.speed("fast") #instead speed to fast
timmy.pensize(10)

def random_move():
  timmy.color(random.choice(colors))
  timmy.setheading(random.choice(directions))
  timmy.forward(25)

while True:
  random_move()

#18.5 Coding Challenge - spirograph
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.speed("fastest")

for deg in range(0,360,5):
  timmy.setheading(deg)
  timmy.color(random_color())
  timmy.circle(100)





screen.exitonclick()