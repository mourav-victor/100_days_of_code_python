## Coffee Machine Project

import random
import os
clear = lambda: os.system('cls') 

import menu
import coffee_maker
import money_machine

menu = menu.Menu()
money_machine = money_machine.MoneyMachine()
coffee_maker = coffee_maker.CoffeeMaker()

while(True):
    options = menu.get_items()
    choice = input(f"What do you want, sir? ({options}): ")

    if choice == "off":
        break

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    if(choice != "espresso" and choice != "latte" and choice != "cappuccino"):
        print("Sorry, we couldnt find this drink")
        continue
    
    drink = menu.find_drink(choice)
    if(not coffee_maker.is_resource_sufficient(drink)):
        print("Sorry, no resources for this drink, try again later")
        continue

    if(money_machine.make_payment(drink.cost)):
        coffee_maker.make_coffee(drink)
