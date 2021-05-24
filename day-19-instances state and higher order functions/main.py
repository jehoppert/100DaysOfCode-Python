from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
  tim.forward(10)

screen.listen()
#onkey is a higher order function, function that takes in a function
screen.onkey(fun=move_forward, key="space")
screen.exitonclick()