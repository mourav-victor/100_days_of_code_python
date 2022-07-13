## Erros and Exceptions

## Examples of errors:
# FileNotFoundError
# KeyError
# IndexError
# TypeError

## Using try/catch the program doesnot crash if there is an error
try:
    file = open("not_a_file.txt")
except FileNotFoundError: # or just except
    print("Error trying to open file")
else:
    print("File opened sucessfully")
finally:
    print("Nice!")