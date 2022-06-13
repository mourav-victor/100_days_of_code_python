## Higher or Lower
import random
import os
clear = lambda: os.system('cls')

def print_gameName():
    game_name = """
    ###############################
    ######  HIGHER OR LOWER  ######
    ###############################
    """
    print(game_name)

# 1. Display the name of the game
print_gameName()

# 2. Create dictinary of persons and followers
insta_dic = {"Neymar" : 175000000, "Mbappe": 71600000, "Cristiano Ronaldo" : 451000000, 
    "Elon Musk" : 3100000, "Snoop Dogg" : 74000000, "Vin Diesel" : 80800000, 
    "LeBron James" : 515000000, "Michael Jordan" : 351000000, "Steph Curry" : 42700000,
    "Axl Rose" : 80400, "Luva de Pedreiro" : 14200000, "Casimiro" : 2700000,
    "Waguinho" : 274000, "Zuckerber" : 9800000, "Jeff Bezos" : 3900000, "Bill Gates" : 7300000}


# 3. Choose a random personality and compares with another, repeatly
score = 0
second_person_name, second_person_followers = random.choice(list(insta_dic.items()))
while(True):
    first_person_name, first_person_followers = second_person_name, second_person_followers
    print(f"Compare A: {first_person_name}")
    print(f"or")
    second_person_name, second_person_followers = random.choice(list(insta_dic.items()))
    print(f"Compare B: {second_person_name}")

    # 4. Ask the user the most popular and verify answer
    answer = ""
    while(answer != "A" and answer != "B"):
        answer = input("Who has more followes? ")

    # 5. If wrong, game over and display score
    #    If right, keep second personality and compares with another, repeaty it so on

    if((answer == "A" and first_person_followers > second_person_followers) or 
        (answer == "B" and first_person_followers < second_person_followers)):
        score += 1
        clear()
        print_gameName()
        print(f"\nYou are right! Current Score: {score}.")

    else:
        print(f"\nGame over! Your score : {score}")
        break


