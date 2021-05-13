#8.1 Coding Challenge - paint area calculator
import math
def paint_calc(height, width, cover):
  #determine number of paint cans to purchase
  num_of_cans = math.ceil((height * width) / cover)
  print(f"You will need {num_of_cans} of paint")

h = int(input("Height of wall: "))
w = int(input("Width of wall: "))
coverage = 5 #5m^2
paint_calc(height = h, width = w, cover = coverage)

#8.2 Coding Challenge - prime number check
def prime_check(number):
  #check to see if a number is prime
  prime = True
  for i in range(2,number):
    if number % i == 0:
      prime = False
  if prime:
    print("It's a prime number")
  else:
    print("It's not a prime number")

n = int(input("Check this number: "))
prime_check(number = n)