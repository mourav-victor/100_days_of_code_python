## Ceaser Cipher

def encode(word, shift):
    encoded_word = ""
    for letter in word:
        encoded_word += chr((ord(letter)+shift-97) % 26 + 97)
    
    return encoded_word

def decode(word, shift):
    decoded_word = ""
    for letter in word:
        decoded_word += chr((ord(letter)-shift-97) % 26 + 97)
    
    return decoded_word

option = input("Wellcome to Ceasar Cipher, what do you want?\n(1) Encode\n(2) Decode\n")
if(option == "1"):
    word = encode(input("Whats it the word to be encrypted? "), 3)
    print(f"Encrypting your word... {word}")
elif(option == "2"):
    word = decode(input("Whats it the word to be decoded? "), 3)
    print(f"Decoding your word... {word}")
else:
    print("Command not found")
