## List Comprehension
# What is it? A method, exclusive to python, to create a list based on another way easier, so reducing code
# Prototype: new_list = [new_item for item in list]
# Prototype: new_list = [new_item for item in list if test]

# Example (1) // using a list
numbers = [1,2,3,4,5]
squared_numbers = [x*x for x in numbers]
print(squared_numbers)

# Example (2) // using a range  
doubled_numbers = [2*x for x in range(1,6)]
print(doubled_numbers)

# Example (3) // using a string
name = 'Victor'
letters = [letter for letter in name]
print(letters)

# Example (4) // Using condictional 
even_numbers = [x for x in numbers if x%2==0]
print(even_numbers)

# Using two variables
sparse_matrice = [1, 0, 0, 20, 4, 0, 0, 0, 0, 0, 12, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 0, 0]
elements = [x for x in sparse_matrice if x != 0]
print(elements)
indexes = [i for i, x in enumerate(sparse_matrice) if x!=0]
print(indexes)