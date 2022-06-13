## Number Guessing Game - Final Project
import random

def print_gameName():
    game_name = """
    ###############################
    #####  NUMBER GUESS GAME  #####
    ###############################
    """
    print(game_name)


print_gameName()
print("A number was chosen randomly between 1 and 100")
number = random.randint(1, 100)
guessed = False
tries = 0

while(not guessed):
    guess = int(input("\nTry to guess it: "))
    tries += 1
    if(guess > number):
        print("Too high")
    if(guess < number):
        print("Too low")
    if(guess == number):
        print(f"YOU GOT IT - after {tries} tries :)")
        guessed = True
    