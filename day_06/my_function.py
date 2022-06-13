def print_style(my_string):
    new_string = ""
    upper = False
    for letter in my_string:
        if(upper):
            new_string += letter.upper()
        else:
            new_string += letter.lower()
        upper = not upper  
    print(new_string)


print("Running function...")
print_style("This is my stylish text")

