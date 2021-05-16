#blackjack game

#House Rules:
#The deck is unlimited in size (equal chances for cards)
#Cards are not removed from the deck as they are drawn (equal probability of being drawn)
#Jack/Queen/King count as 10
#Ace is either 1 or 11
#cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
import os
import random
import blackjack_art

#define methods
def deal_card():
  """
  Returns a random choice from the cards list
  """
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  return random.choice(cards)

def calculate_score(cards):
  """
  Calculates the total of the hand of cards
  """
  if sum(cards) > 21 and 11 in cards:
    #replace 11 with 1 if over 21
    cards.remove(11)
    cards.append(1)

  return sum(cards)

def check_score(user_cards, dealer_cards):
  """
  Checks the users and dealers cards for the outcome of the game
  """
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)
  if user_score == dealer_score:
    print(f"Cards: {user_cards} - score: {user_score}")
    print(f"Dealer Cards: {dealer_cards} - score: {dealer_score}")
    print("You lose, tie goes to dealer")
  elif dealer_score == 21:
    print(f"You lose, unlucky dealer blackjack {dealer_cards}")
  elif user_score == 21:
    print(f"You win, nice blackjack {user_cards}")
  elif user_score > 21:
    print(f"You lose, you busted")
  elif dealer_score > 21:
    print(f"You win, dealer busted {dealer_cards}")
  elif user_score > dealer_score:
    print(f"Cards: {user_cards} - score: {user_score}")
    print(f"Dealer Cards: {dealer_cards} - score: {dealer_score}")
    print("You win, you have the highest score")
  else:
    print(f"Cards: {user_cards} - score: {user_score}")
    print(f"Dealer Cards: {dealer_cards} - score: {dealer_score}")
    print("You lose, dealer has the highest score")


def game():
  """
  Runs the blackjack game
  """
  print(blackjack_art.logo)

  user_cards = []
  dealer_cards = []

  #start game logic
  for i in range(2):
    #create starting card list for user & dealer
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

  #get the starting scores
  user_score = calculate_score(user_cards)
  dealer_score = calculate_score(dealer_cards)

  #display info to the player
  print(f"You have {user_cards} - score: {user_score}")
  print(f"Dealer has [{dealer_cards[0]}, *]")

  game_over = False
  user_playing = True
  while not game_over:
    if dealer_score == 21 or user_score == 21 or user_score > 21:
      game_over = True
    elif user_playing:
      hit = input("Would you like to draw another card? Yes or No?: ")
      if hit.lower() == "yes":
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"Cards: {user_cards} - score: {user_score}")
      else:
        user_playing = False
    
    elif dealer_score < 17:
      dealer_cards.append(deal_card())
      dealer_score = calculate_score(dealer_cards)
      print(f"Dealer Cards: {dealer_cards} - score: {dealer_score}")
    else:
      game_over = True

  check_score(user_cards, dealer_cards)

  cont = input("Do you want to play again? Yes or No?: ")
  if cont.lower() == "yes":
    os.system('cls' if os.name == 'nt' else 'clear')
    game()

game()