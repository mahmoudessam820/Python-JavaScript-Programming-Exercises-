# Python Quiz (22) 😉
# What is the output of this code and why🤔?


variable  = [1, 2] + [3, 4] * 2

print(variable)


#Output

# a- [1, 2, 3, 4, 3, 4]
# b- [1, 2, 3, 4, 1, 2, 3, 4]
# c- [2, 4, 6, 8]
# d- [2, 4, 6, 8, 6, 8]


# Explanation:

# Creating a list by concatenating [1, 2] with [3, 4] multiplied by 2. 
# The * operator with lists repeats the elements in the list by the specified number of times.
# So, [1, 2] + [3, 4] * 2 results in [1, 2] + [3, 4, 3, 4], which equals [1, 2, 3, 4, 3, 4].

# So, the correct output is: a- [1, 2, 3, 4, 3, 4]