from turtle import Screen
from snake import Snake
import time
#setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) #turn off trace force call of update

#create snake object
snake = Snake()

#listen for snake movement inputs
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

#start game
on = True
while on:
  time.sleep(.1)
  screen.update()
  
  snake.move() #start moving the snake

  







#part2:
#detect collision with food
#create a scoreboard
#detect collision with wall
#detect collision with self

screen.exitonclick()