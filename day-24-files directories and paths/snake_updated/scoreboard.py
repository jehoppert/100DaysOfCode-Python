from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = self.read_highscore()
    self.hideturtle()
    self.goto(x=0, y=280)
    self.penup()
    self.color("white")
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.write(f"SCORE: {self.score} HIGH SCORE: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

  def increase_score(self):
    self.score += 1
    self.update_scoreboard()

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.save_highscore()
    self.score = 0
    self.update_scoreboard()

  def read_highscore(self):
    with open("snake_highscore.txt", mode="r") as file:
      return int(file.read())

  def save_highscore(self):
    with open("snake_highscore.txt", mode="w") as file:
      file.write(f"{self.high_score}")

  #def game_over(self):
  #  self.goto(x=0, y=0)
  #  self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)