# Python Quiz (16) 😉
# What is the output of this code and why 🤔?


a = {1, 2, 3, 4}
b = {3, 4, 5}
c, *d = a & b 

print(d)

# Output 

# a - [4]
# b - [3, 4]
# c - 4 
# d - [3]


# Explanation:


# a = {1, 2, 3, 4}: This line declares a set named a and initializes it with the elements 1, 2, 3, and 4.
# b = {3, 4, 5}: This line declares a set named b and initializes it with the elements 3, 4, and 5.
# c, *d = a & b: This line performs a set intersection operation between sets a and b using the & operator. 
# The intersection of two sets returns a new set with elements that are common in both sets. 
# The result is assigned to two variables: c and d. 
# The variable c will store an element common to both sets (c = 3 in this case), and d will store the remaining elements from the intersection (d = [4] in this case). 
# The use of the * operator before d is called the "extended iterable unpacking" syntax and allows d to capture all remaining elements from the intersection.
# Finally, the code prints the value of d, which will be [4]. 
