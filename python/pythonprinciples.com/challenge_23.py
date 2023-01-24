"""
    level of challege 5/10

    Counting parameters

    Define a function param_count that takes a variable number 
    Of parameters. 
    
    The function should return the number of arguments it was 
    called with.

    For example:

    param_count() should return 0, 
    while param_count(2, 3, 4) should return 3.

"""

def param_count(*args):
    return len(args)
print(param_count(1, 3, 4, 5))