## Coffee Machine Project

import random
import os
clear = lambda: os.system('cls')

def printProjectName():
    game_name = """
    ###############################
    ######  COFFEE  MACHINE  ######
    ###############################
    """
    print(game_name)

def printRessources(resources, money):
    print(f" - Water: {resources['water']}ml")
    print(f" - Milk: {resources['milk']}ml")
    print(f" - Coffee: {resources['coffee']}g")
    print(f" - Money: ${money}")
    
def checkRessources(MENU, resources, drink):
    notEnough = False
    for ingridient in MENU[drink]["ingredients"]:

        if(MENU[drink]["ingredients"][ingridient] > resources[ingridient]):
            print(f"Sorry there is not enough {ingridient}.")
            notEnough = True

    return notEnough

def processCoins():
    coins = input("How are you paying? (25/10/5/1): ")
    coins_value = [0.25, 0.10, 0.05, 0.01]
    money_paid = 0

    if "/" in coins:
        coins = coins.split("/")
    elif " " in coins:
        coins = coins.split(" ")
    else:
        print("Wrong format")
        return 0

    for i in range(len(coins)):
        money_paid += int(coins[i]) * coins_value[i]

    return money_paid

def recalculateResources(MENU, resources, drink):
    for ingridient in MENU[drink]["ingredients"]:
        resources[ingridient] -= MENU[drink]["ingredients"][ingridient]

    return resources


# 1. Display the name of the game
printProjectName()

# 2. Set machine ressources and drink needs
machine_money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# 3. Asking customer service and loop throught it
while(True):

    option = input("What would you like? (espresso/latte/cappuccino): ")

    # 4. Turn off the Coffee Machine by entering “off” to the prompt.
    if(option == "off"):
        break 

    # 5. Print report.
    if(option == "report"):
        printRessources(resources, machine_money)
        continue

    # 6. Check if drink is valid
    if(option != "espresso" and option != "latte" and option != "cappuccino"):
        print("Drink unknown")
        continue

    # 7. Check resources sufficient?
    drink = option
    drink_cost = MENU[drink]['cost']
    if(checkRessources(MENU, resources, drink)):
        break

    # 8. Process coins.
    money_paid = processCoins()
    if(not money_paid):
        break
    
    # 9. Check transaction successful?
    if(money_paid < drink_cost):
        print("Not enough money, sorry")
        continue
    
    change = round(money_paid - drink_cost, 2)
    print("\n------ Bill------")
    print(f"| Your money: {money_paid}")
    print(f"| Drink cost: {drink_cost}" )  
    print(f"|     Change: {change}" )
    print("----------------- \n")

    # 10. Make coffee
    print("Here is your coffee, sir!")
    print(f'Old money {machine_money}')
    print(f'Old money {resources}')
    machine_money += (change)
    resources = recalculateResources(MENU, resources, drink)
    print(f'Current money {machine_money}')
    print(f'Current money {resources}')
    print()
