from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0) #turn off trace force call of update

#create snake object
snake = Snake()
#create food object
food = Food()
scoreboard = Scoreboard()

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

  #detect collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    scoreboard.increase_score()

  #detect collision with wall
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    scoreboard.reset()
    snake.reset()

  #detect collision with tail with list slicing [::-1] to reverse
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()





screen.exitonclick()