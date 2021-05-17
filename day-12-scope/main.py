#12.1 Coding Challenge - testing of scope
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

#local scope
def drink_potion():
  potion_strength = 2 #local
  print(potion_strength)

drink_potion()
#print(potion_strength) #doesnt work since it is local to the function

#global scope
player_health = 10 #global
def drink_health_potion():
  potion_strength = 2
  print(player_health)

drink_health_potion()
print(player_health)

#12.2 Coding Challenge - modify gloabl var
enemies = 1
def increase_enemies():
  global enemies #allows modification of global var
  enemies += 1
  print(enemies)

increase_enemies()

enemies = 1
def increase_enemies():
  global enemies #allows modification of global var
  return enemies + 1

enemies = increase_enemies()
print(enemies)

#12.3 Coding Challenge - global contants
PI = 3.1415
URL = "https://www.google.com"
TWITTER_HANDLE = "@jehoppert"