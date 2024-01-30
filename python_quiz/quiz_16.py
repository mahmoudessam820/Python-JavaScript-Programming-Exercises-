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

# The code starts by creating two sets, a and b.
# Set a contains the elements 1, 2, 3, and 4, while set b contains the elements 3, 4, and 5.
# The next line c, *d = a & b performs the intersection operation between sets a and b. 
# The intersection operation (&) returns a new set that contains the common elements present in both sets.
# The interesting part is the syntax c, *d. Here, c is a single variable assigned to the first element of the intersection set (in this case, 3).
# The asterisk (*) before d is used to assign the remaining elements of the intersection set to d.
# Finally, the code prints the value of d, which will be [4]. 
# This is because d holds the remaining elements of the intersection set other than the first element (3).

