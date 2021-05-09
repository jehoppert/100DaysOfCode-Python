#3.1 Coding Challenge - Odd or Even?
number = int(input("Which number do you want to check?\n"))
mod = number%2 #get mod/remainder of the division
if mod == 1:
  print("This is an odd number")
else:
  print("This is an even number") 

#3.2 Coding Challenge - BMI 2.0
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = round(weight / height**2)
if BMI < 18.5:
  description = "underweight"
elif BMI < 25:
  description = "normal weight"
elif BMI < 30:
  description = "slightly overweight"
elif BMI < 35:
  description = "obese"
else:
  description = "clinically obese"
print(f"Your BMI is {BMI}, you are {description}")

#3.3 Coding Challenge - Leap Year 
year = int(input("Which year do you want to check?\n"))
if year%4 == 0:
  if year%100 == 0:
    if year%400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

#3.4 Coding Challenge - Pizza Order Practice
print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S, M, or L?\n")
add_pepperoni = input("Do you want pepperoni? Y or N?\n")
extra_cheese = input("Do you want extra cheese? Y or N?\n")
bill = 0

#size check
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else: #large
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else: #medium or large
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is ${bill}")

#3.5 Coding Challenge - Love Calculator
print("Welcome to the love calculator!")
#covert to all lowercase letters
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()
join_name = name1 + name2
#true love 
true_score = join_name.count("t") + join_name.count("r") + join_name.count("u") + join_name.count("e")
love_score = join_name.count("l") + join_name.count("o") + join_name.count("v") + join_name.count("e")

love_score = str(true_score) + str(love_score)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score > 40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together")
else:
  print(f"Your score is {love_score}")