"""
    level of challenge 4/10

    Boolean and

    Define a function named triple_and that takes 
    three parameters and returns True only if they are all True 
    and False otherwise.


"""

# My solution 

def triple_and(one, tow, three):
    
    if one == True and tow == True and three == True:
        return True
    else:
        return False

print(triple_and(True, True, True))

# Aonther solution 

def triple_and(a, b, c):
    return a and b and c