#coffee machine project 
from coffee_machine_data import menu,resources

def print_report():
  print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}g
    Money: ${'{0:.2f}'.format(resources['money'])}
  """)

def check_resources(drink):
  for ingredient in menu[drink]["ingredients"]:
    if resources[ingredient] - menu[drink]["ingredients"][ingredient] < 0:
      print(f"Sorry there is not enough {ingredient}")
      return False
  return True


def process_coins():
  print("Please insert coins")
  q = int(input("Insert how many quarters?: "))
  d = int(input("Insert how many dimes?: "))
  n = int(input("Insert how many nickles?: "))
  p = int(input("Insert how many pennies?: "))
  total = (q * .25) + (d * .10) + (n * .05) + (p * .01)
  return total

def process_transaction(drink, total):
  global resources
  if menu[drink]["cost"] <= total:
    resources['money'] += menu[drink]["cost"]
    if total > menu[drink]["cost"]:
      change = '{0:.2f}'.format(total - menu[drink]["cost"])
      print(f"Here is ${change} in change")
  else:
    print("Sorry that's not enough money. Money refunded.")
    return False
  return True

def make_coffee(drink):
  global resources
  for ingredient in menu[drink]["ingredients"]:
    resources[ingredient] -= menu[drink]["ingredients"][ingredient]
  print(f"Here is your {drink}. Enjoy!")

machine_on = True
while machine_on:
  selection = input("What would you like? (espresso/latte/cappuccino): ").lower()

  #maintenance option to turn off the machine (end program)
  if selection == "off":
    machine_on = False
  #maintenance option to view current resource levels
  elif selection == "report":
    print_report()
  elif selection in menu:
    #TODO: check transaction, make coffee
    if check_resources(selection):
      total = process_coins()
      if process_transaction(selection, total):
        make_coffee(selection)

  else:
    print("Invalid selection")