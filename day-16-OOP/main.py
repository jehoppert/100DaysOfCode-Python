#16.1 Coding Challenge - Working with tutle objects
from turtle import Turtle, Screen

#construct a class object
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DarkSeaGreen")
timmy.forward(100)

my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick()

#16.2 Coding Challenge - install and use module 
#pip3 install prettytable
from prettytable import PrettyTable 

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

