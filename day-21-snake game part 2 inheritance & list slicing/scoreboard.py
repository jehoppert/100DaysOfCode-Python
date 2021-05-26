from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.hideturtle()
    self.goto(x=0, y=280)
    self.penup()
    self.color("white")
    self.update_scoreboard()

  def update_scoreboard(self):
    self.write(f"SCORE: {self.score}", move=False, align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.clear()
    self.update_scoreboard()

  def game_over(self):
    self.goto(x=0, y=0)
    self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)