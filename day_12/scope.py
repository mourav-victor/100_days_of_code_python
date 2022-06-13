## Lets try local and global scope

PI = 3.14159265 # constant variable convenction => All CAPSLOCK
enemies = 0
friends = 0
level = 0

def add():
    global friends
    enemies = 1
    friends = 1

    return [enemies, friends]

print(f"You have {enemies} enemies and {friends} friends")
add()
print(f"You now have {enemies} enemies and {friends} friends")
print("Or, using return ...")
print(f"You now have {add()[0]} enemies and {add()[1]} friends")
