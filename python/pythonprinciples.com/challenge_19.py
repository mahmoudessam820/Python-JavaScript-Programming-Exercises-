"""
    level of challene 5/10

    Writing short code

    Define a function named convert that takes a list of numbers
    as its only parameter and returns a list of each number converted to a string.

    For example:
    the call convert([1, 2, 3]) should return ["1", "2", "3"].

    What makes this tricky is that your function body must only contain a single line of code.


"""

# My solution 

def convert(lists): return [str(con_list) for con_list in lists]
print(convert([1, 2, 3]))


# Another solution 

# using a list comprehension
def convert(ns):
    return [str(n) for n in ns]

# using map
def convert(ns):
    return list(map(str, ns))