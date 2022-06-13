import random
from hangman_draws import hangsman_stage
from hangman_words import possible_words


def print_list(word):
    for item in word:
        print(item, end=' ')
    print("\n")



print("Wellcome to Hangman's game, also known as Jogo da Forca")
#possible_words = ["papagaio", "edificio", "raquete", "ventilador", "foca"]
lifes = 6
guessed = False

word = random.choice(possible_words)
partial_word = ['_'] * len(word)

while(not guessed):
    # Get user input
    print(hangsman_stage[lifes])
    print_list(partial_word)
    guess = input("Choose a letter: ")
    correct_guess = False

    # Search for letter in word and fill blank spaces
    for idx in range(0,len(word)):
        letter = word[idx]
        if guess == letter:
            partial_word[idx] = guess
            correct_guess = True

    # Compute lifes and verify if player still have lifes
    if not correct_guess:
        lifes = lifes - 1
        if lifes == 0:
            break

    # Print current result and lives
    print(f"Remaining lifes: {lifes}")
    #print_list(partial_word)

    # Verify if game is finished
    guessed = True
    for item in partial_word:
        if item == "_":
            guessed = False


if  guessed:
    print_list(partial_word)
    print("Awesome, you beat us!!")
else:
    print(hangsman_stage[0])
    print("YOU HAVE LOST")
    print(f"The word was {word}")

        