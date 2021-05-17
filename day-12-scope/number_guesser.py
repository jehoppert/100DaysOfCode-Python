import random
import number_guesser_art

game_over = False

def check_guess(number, guess):
  global turns
  global game_over
  if number > guess:
    print("Too low")
    turns -= 1
  elif number < guess:
    print("Too high")
    turns -= 1
  else:
    print(f"You guessed the correct number - {number}")
    game_over = True

  if turns < 1:
    print(f"You ran out of guesses. The number was {number}")

number = random.randint(1,100)

print(number_guesser_art.logo)
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == "hard":
  turns = 5
else:
  turns = 10

while turns > 0 and not game_over:
  print(f"You have {turns} guesses remaining")
  guess = int(input("Make a guess: "))
  check_guess(number, guess)