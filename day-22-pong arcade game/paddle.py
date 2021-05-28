from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

  def __init__(self, cordinates):
    #create paddle object
    super().__init__()
    self.shape("square")
    self.penup()
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.color("white")
    self.speed("fastest")
    self.goto(cordinates)

  def up(self):
    self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
    
  def down(self):
    self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)
    