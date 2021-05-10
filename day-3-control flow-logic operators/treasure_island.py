print('''
         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|
''')
print("Welcome to treasure island")
print("Your mission is to find the treasure")

path1 = input("You wash up onto the island and see a fork in the road. Which direction do you go? Left or Right?\n").lower()

if path1 == "left":
  path2 = input("You come to a view of the ocean and see something in the water. Do you go out and investigate? Swim or Wait?\n").lower()

  if path2 == "wait":
    path3 = input("You finally stumble upon a group of doors. Which do you choose? Red, Blue, or Yellow?\n")

    if path3 == "yellow":
      print("You found the hidden treasure! A pirates life for you!")

    else:
      if path3 == "red":
        print("You are burned alive by a blast of fire. Game Over.")
      elif path3 == "blue":
        print("You are eaten by a mysterious creature. Game Over.")
      else:
        print("You failed to choose a door and died of starvation. Game Over.")

  else:
    print("You get attacked by a shark. Game Over.")

else:
  print("You fall into a sinkhole. Game Over.")





