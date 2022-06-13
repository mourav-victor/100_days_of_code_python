## BlackJack project
import random

def calculate_sum(cards):
    bj_sum = 0
    for card in cards:
        if card == 'J' or card == 'Q' or card == 'K':
            bj_sum += 10
        else:
            bj_sum += card
    
    if((bj_sum > 21) and (11 in cards)):
        bj_sum -= 10

    return bj_sum

def veredict(your_cards, cpu_cards):
    if calculate_sum(cpu_cards) > 21:
        print('CPU exceed 21, you won')
    elif calculate_sum(your_cards) > calculate_sum(cpu_cards):
        print("You won, good work!")
    elif calculate_sum(your_cards) == calculate_sum(cpu_cards):
        print("Thats a draw, nothing bad!")
    else:
        print("You lost, try again ...")

def hasBlackJack(your_cards, cpu_cards):
    if calculate_sum(cpu_cards) == 21:
        print("CPU BlackJacked, you lost!")
        quit()
    if calculate_sum(your_cards) == 21:
        print("What an amazing BlackJack, you won")
        quit()

game_name = """"
###############################
#####  AWESOME BLACKJACK  #####
###############################
"""
print(game_name)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
input("Press Enter to receive cards ...")
your_cards = random.choices(cards, k=2)
cpu_cards = random.choices(cards, k=1)
print(f"Your cards: {your_cards} - {calculate_sum(your_cards)}")
print(f"CPU cards: {cpu_cards}")
hasBlackJack(your_cards, cpu_cards)
lost = False

while(input("\nDo you want another card? (y/n) ") == 'y'):
    your_cards.append(random.choice(cards))
    print(f"Your cards: {your_cards} - {calculate_sum(your_cards)}")
    if (calculate_sum(your_cards) > 21):
        lost = True
        break
    
if lost:
    print("YOU LOST")
else:
    print("Lets see the results...")
    print(f"Your cards: {your_cards} - {calculate_sum(your_cards)}")
    while(calculate_sum(cpu_cards) < 17):
        cpu_cards.append(random.choice(cards))
    print(f"CPU cards: {cpu_cards} - {calculate_sum(cpu_cards)}")
    print()
    
    veredict(your_cards, cpu_cards)
