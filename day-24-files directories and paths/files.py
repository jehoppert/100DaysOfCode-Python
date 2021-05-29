#file = open("my_file.txt")
#contents = file.read()
#print(contents)
#file.close()

#read
with open("my_file.txt", mode="r") as file:
  contents = file.read()
  print(contents)

#write - will create if it doesnt exist 
with open("my_file.txt", mode="w") as file:
  file.write("New text")
  
#append
with open("my_file.txt", mode="a") as file:
  file.write("\nNew text")

#absolute file path - starts at root (/)
#relative file path - starts where we are (./ or ../) 

#using absolute file path
with open("/Users/jehoppert/Documents/100DaysOfCode-Python/day-24-files directories and paths/test_folder/my_file_inner.txt", mode="r") as file:
  contents = file.read()
  print(contents)

#using relative file path
with open("./my_file.txt", mode="r") as file:
  contents = file.read()
  print(contents)