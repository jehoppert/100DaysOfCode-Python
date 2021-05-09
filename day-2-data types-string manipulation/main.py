# 2.1 Coding Challenge - data types
two_digit_number = input("Enter a two digit number: ")
#print(type(two_digit_number))
print(int(two_digit_number[0]) + int(two_digit_number[1]))

#2.2 Coding Challenge - BMI Calculator
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
bmi = weight / height**2
print(int(bmi))

#2.3 Coding Challenge - Life in Weeks
age = int(input("What is your current age?\n"))
#calculate years left until you reach 90
years_left = 90 - age
#calculate days, weeks, and months we have left to live
months = years_left * 12
weeks = years_left * 52
days = years_left * 365
#print output using f strings to place in values
print(f"You have {days} days, {weeks} weeks, and {months} moths left...")