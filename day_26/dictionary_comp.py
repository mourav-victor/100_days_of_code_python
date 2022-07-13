## Dictionary Comprehension
# What is it? A method, exclusive to python, to create a dict based on another way easier, so reducing code
# Prototype: new_dict = {new_key:new_value for item in list}
# Prototype: new_dict = {new_key:new_value for (key,value) in dict.items()}
# Prototype: new_dict = {new_key:new_value for (key,value) in dict.items() if test}

import random

# Example (1)
names = ["Victor", "Kbsa", "Raul"]
dict_score = {item:random.randint(1,10) for item in names}
print(dict_score)

# Example (2)
dict_score_over_100 = {key:value*10 for (key,value) in dict_score.items()}
print(dict_score_over_100)

# Example (3)
dict_score_approved = {key:value for (key,value) in dict_score_over_100.items() if value >= 60}
print(dict_score_approved)