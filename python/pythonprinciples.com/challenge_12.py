"""
    level of challenge 3/10

    Divisible by 3

    - Define a function named div_3 that returns True 
    - If its single integer parameter is divisible by 3 
    - And False otherwise.

    For example:

    - div_3(6) is True because 6/3 does not leave any remainder.
    - However div_3(5) is False because 5/3 leaves 2 as a remainder.

"""

# My solution

def div_3(number):
    if number % 3:
        return False
    else:
        return True

print(div_3(6))

# Another solution

def div_3(n):
    return n % 3 == 0