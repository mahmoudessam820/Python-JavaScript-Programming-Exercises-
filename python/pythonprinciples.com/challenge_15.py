"""
    level of challenge 4/10

    Up and down

    Define a function named up_down that takes a single number 
    As its parameter. 
    Your function return a tuple containing two numbers
    The first should be one lower than the parameter, 
    And the second should be one higher.

    For example:
    calling up_down(5) should return (4, 6)

"""

# My Solution 

def up_down(number):
    down = number - 1
    up = down + 2
    return (down, up)
print(up_down(6))


# Another Solution

def up_down(x):
    return (x-1, x+1)