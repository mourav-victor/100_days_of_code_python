## Create a strong password
import random 

nb_letters = int(input("How many letters?"))
nb_symbols = int(input("How many symbols?"))
nb_numbers = int(input("How many numbers?"))

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&"

a = random.choices(letters, k=nb_letters) + random.choices(numbers, k=nb_numbers) + random.choices(symbols, k=nb_symbols)
random.shuffle(a)
password = ''.join(a)
print(password)