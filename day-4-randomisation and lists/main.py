#4.1 Coding Challenge - random coin toss 
import random
print("Virtual coin toss")
r = random.randint(0,1)
if r > 0:
  print("Heads")
else:
  print("Tails")

#4.2 Coding Challenge - lists banker routlette
import random
names_string = input("Give me everybody's names, seperated by a comma\n")
names = names_string.split(", ")
#could use random.choice(names) to pick an item at random
print(f"{names[random.randint(0,len(names)-1)]} is paying the bill today!")

#4.3 Coding Challenge - list/error Treasure map
row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]
map = [row1, row2, row3] #nested list
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Column and Row?\n")
column = int(position[0])
row = int(position[1])
map[row-1][column-1] = "x"
print(f"{row1}\n{row2}\n{row3}")
