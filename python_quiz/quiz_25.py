# Python Quiz (25) 😉
# What is the output of this code and why🤔?


def conditions(data):

    if all(data):
        return "yes"
    elif not any(data):
        return "no"
    else: 
        return "I don't know"
    

values = [True, False, True, False]

print( conditions(values) )


# Output

# a- yes
# b- no
# c- I don't know
# b- Error


# Explanation:

# Defines a function conditions that takes a list data as input and returns a string based on certain conditions evaluated on the elements of the list. 
# This if statement checks if all the elements in the data list evaluate to True.
# The all() function returns True if all elements in the iterable are True, and False otherwise.
# If all elements are True, the function returns "yes".
# This elif statement checks if none of the elements in the data list evaluate to True. 
# The any() function returns True if at least one element in the iterable is True, and False if all elements are False.
# So not any(data) checks if all elements are False.
# If none of the above conditions are met, it means there are both True and False values in the data list. In this case, the function returns "I don't know".

# Given the values list [True, False, True, False], it contains both True and False elements,

# So the output will be "I don't know"

# The correct output is: c- I don't know