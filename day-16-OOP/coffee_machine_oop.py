#OOP Coffee Machine
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

on = True
while on:
  prompt = input(f"What would you like? {menu.get_items()}: ").lower()

  if prompt == "off":
    on = False
  elif prompt == "report":
    coffee_maker.report()
    money_machine.report()
  elif prompt in menu.get_items().split('/'):
    drink = menu.find_drink(prompt) 
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)
  else:
    print("Invalid selection")