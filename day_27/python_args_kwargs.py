## Python arguments


# (1) Default arguments
def increase(number, quant = 1):
    return (number + quant)

print(increase(10))
print(increase(10, 10))
print()


# (2) Flexible and iterable number of arguments: *args
def add(*args):  
    print(args) # args is a tuple!
    itens_sum = 0
    for item in args:
        itens_sum += item

    return itens_sum
    # return none is default

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# (3) *kwargs (Keyword Arguments)
def calculate(n, **kwargs):  
    print(kwargs) # args is a dict!
    
    n += kwargs["add"] # or n += kwargs.get("add")
    n *= kwargs["multiply"] # or n *= kwargs.get("multiply")

    return n

print(calculate(2, add=10, multiply=10))
