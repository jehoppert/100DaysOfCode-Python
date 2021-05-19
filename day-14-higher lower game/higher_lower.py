#break down the problem
#make todo list for project
#turn todo into comments
#code this shit

import higher_lower_art
from higher_lower_game_data import data
import os
import random

def compare_follower_count(followers_A, followers_B):
  """
  Compare the follower count of two people
  Returns: 'a' or 'b'
  """
  if followers_A > followers_B:
    return "a"
  else:
    return "b"

 #generate art
print(higher_lower_art.logo)

#init global variables
score = 0
playing = True

#chose the first two people to compare
person_A = random.choice(data)
person_B = random.choice(data)

#start playing the game until they lose
while(playing):
  #quick check to see if A and B are the same person
  while person_A == person_B:
    person_B = random.choice(data)

  #display people to compare to user
  print(f"Compare A: {person_A['name']}, a {person_A['description']}, from {person_A['country']}")
  print(higher_lower_art.vs)
  print(f"Against B: {person_B['name']}, a {person_B['description']}, from {person_B['country']}")
  
  #get guess for who has more followers
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  #check whether A or B has more followers
  most_followers = compare_follower_count(person_A['follower_count'], person_B['follower_count'])

  os.system('clear') #for linux and mac
  print(higher_lower_art.logo)

  if guess == most_followers:
    score += 1
    print(f"You're right! Current score: {score}")
    #A swaps with B on a correct guess
    person_A = person_B
    person_B = random.choice(data)
    
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    playing = False #game over