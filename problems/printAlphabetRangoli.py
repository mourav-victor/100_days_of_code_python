## Alphabet Rangoli
# ex.: (given size = 3)
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

size = 6
len = (size * 2 - 1) * 2 -1

# step 1 - store letters of the alphabet
alphabet_letters = "abcdefghijklmnopqrstuvwxyz"
letters = alphabet_letters[:size]
letters = letters[::-1]

# step 2 - drawning upper side pyramid
for i in range(0,size):
    row_letters = letters[:i+1] + letters[:i][::-1]
    row_letters = "-".join(row_letters)
    print(row_letters.center(len, "-"))

# step 2 - drawning lower side pyramid
for i in range(size-2,-1,-1):
    row_letters = letters[:i+1] + letters[:i][::-1]
    row_letters = "-".join(row_letters)
    print(row_letters.center(len, "-"))


