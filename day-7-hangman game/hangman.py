import os
import random
import hangman_words #prefix - hangman_words.word_list
#import hangman_words as hw #prefix - hw.word_list
#from hangman_words import * #no prefix - word_list
#from hangman_words import word_list #import specific item - word_list
import hangman_art

lives = 6 #corresponds to stages list
end_of_game = False

#Randomly choose a word from the word_list and assign it to a var
chosen_word = random.choice(hangman_words.word_list)
#print(f"Chosen word is: {chosen_word}") #test

#print the starting logo display for the game
print(hangman_art.logo + "\n\n")

#create an empty list for display composed of '_' for each letter in chosen_word
display = []
for _ in chosen_word: #use _ since we are not using the values
  display.append("_")

while not end_of_game:
  #Ask the user to guess a letter and assign their answer to a var
  guess = input("Guess a letter: ").lower()

  os.system('cls' if os.name == 'nt' else 'clear')

  if guess in display:
    print(f"You already guessed {guess}, try a different letter")

  else:
    #check if the guessed letter is one of the letters in the chosen_word and reveal it
    for idx in range(len(chosen_word)):
      if guess == chosen_word[idx]:
        display[idx] = guess

    if guess not in display:
      lives -= 1
      print(f"The letter {guess} is not in the word, you lost a life")

    #show the revealed values to the user
    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

    #if we found all the letters in the chosen_word
    if "_" not in display:
      end_of_game = True
      print("You won!")

    #if we run out of lives
    if lives < 1:
      end_of_game = True
      print(f"You lose, the word was {chosen_word}")

