#FileNotFound
#with open("./fake_file.txt") as file:
#  file.read()

#KeyError
#fake_dictionary = {"key":"value"}
#value = fake_dictionary["non_existent_key"]

#IndexError
#fake_list = ["Apple", "Bannana"]
#fake = fake_list[3]

#TypeError
#error_text = "abc"
#print(error_text + 5)

#try, except, else, finally
"""
try:
  file = open("./error_file.txt")
  error_dict = {"key":"value"}
  print(error_dict["fake"])

except FileNotFoundError:
  file = open("./error_file.txt", "w")
  file.write("Something")

except KeyError as error_message:
  print(f"That key doesnt exist: {error_message}")

else:
  content = file.read()
  print(content)

finally:
  file.close()
  print("File closed")
  raise TypeError("I made this error up")


height = float(input("Hieght: "))
weight = int(input("Weight: "))

if height > 3:
  raise ValueError("Human height is over 3 meters")

bmi = weight / height ** 2

print(bmi)


#Coding Challenge 30.1 - IndexError Handling
fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
  try:
    fruit = fruits[index]
  except IndexError:
    print("Fruit pie")
  else:
    print(fruit + " pie")

make_pie(4)
"""
#Coding Challenge 30.2 - KeyError Handling
facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass #0 likes
    

print(total_likes)