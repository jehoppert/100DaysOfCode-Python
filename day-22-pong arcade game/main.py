from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#init screen for game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_player = Paddle((350,0))
left_player = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=right_player.up, key="Up")
screen.onkey(fun=right_player.down, key="Down")
screen.onkey(fun=left_player.up, key="w")
screen.onkey(fun=left_player.down, key="s")

on = True
while on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #detect collision with wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #detect collision with paddles
  if ball.distance(right_player) < 50 and ball.xcor() > 320 or ball.distance(left_player) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  #detect if ball was missed by a paddle and reset (right missed)
  if ball.xcor() > 380:
    scoreboard.l_point()
    ball.reset_position()

  #left missed
  if ball.xcor() < -380:
    scoreboard.r_point()
    ball.reset_position()
    

screen.exitonclick()