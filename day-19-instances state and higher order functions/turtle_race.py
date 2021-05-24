from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [75,45,15,-15,-45, -75]

#instances and different states for the turtle objects
turtles = {}

for idx in range(len(colors)):
  turtles[colors[idx]] = Turtle(shape="turtle")
  turtles[colors[idx]].color(colors[idx])
  turtles[colors[idx]].penup()
  turtles[colors[idx]].goto(x=-200, y=y_pos[idx])

racing = True
while racing:
  for turtle in turtles:
    if turtles[turtle].xcor() > 230:
      racing = False
      winning_color = turtles[turtle].pencolor()
      if winning_color == user_bet:
        print(f"You won! The {winning_color} turtle is the winner!")
      else:
        print(f"You lost! The {winning_color} turtle is the winner!")
    turtles[turtle].forward(random.randint(0,10))


screen.exitonclick()