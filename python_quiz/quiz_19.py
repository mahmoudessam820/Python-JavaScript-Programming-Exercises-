# Python Quiz (19) 😉
# What is the output of this code and why🤔?


a = {1, 2, 3}
b = {4, 5, 6}

print(*(a and b))

# Output

# a- 1, 2, 3
# b- 4, 5, 6
# c- 1, 2, 3, 4, 5, 6
# d- [4, 5, 6]


# Explanation:

# a = {1, 2, 3}
# b = {4, 5, 6}
# Here, two sets a and b are defined. 
# Sets are unordered collections of unique elements in Python. In this case, a contains elements 1, 2, and 3, and b contains elements 4, 5, and 6.

# print(*(a and b))
# This line prints the elements of the intersection of sets a and b.
# In Python, the and operator between two sets returns the second set if the first set is not empty. 
# Otherwise, it returns the first set.
# So, when you use (a and b), if a is not empty (which it isn't in this case), Python evaluates this expression to b. 
# Therefore, the intersection of a and b is effectively b.
# The * operator used with print unpacks the elements of the set b and passes them as separate arguments to the print function. 
# And the output of this code will be the elements of set b, which are 4, 5, and 6

# Therefore, the correct answer is: b- 4, 5, 6