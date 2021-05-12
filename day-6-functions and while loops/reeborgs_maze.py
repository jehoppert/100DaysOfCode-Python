#Reeborg's world - escape the maze

def turn_right():
  turn_left()
  turn_left()
  turn_left()

#find a wall so we can put it on the right side
while front_is_clear():
  move()
turn_left()

while not at_goal():
  if right_is_clear():
    turn_right()
    move()
  elif front_is_clear():
    move()
  else:
    turn_left()