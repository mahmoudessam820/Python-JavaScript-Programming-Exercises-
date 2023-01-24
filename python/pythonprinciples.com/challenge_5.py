"""
    level of challenge = 2/10

    Type check

    Write a function named only_ints that takes two parameters. 
    Your function should return True if both parameters are integers, and False otherwise.

    For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.

"""

# My solution 

def only_ints(num_1, num_2):
    if type(num_1) == int and type(num_2) == int:
        return True
    else: 
        return False
print(only_ints("tito", 2)) 


# Another soultion 

def only_ints(a, b):
    return type(a) == int and type(b) == int
    