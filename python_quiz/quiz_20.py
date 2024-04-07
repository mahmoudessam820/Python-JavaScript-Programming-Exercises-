# Python Quiz (20) 😉
# What is the output of this code and why🤔?



a = [8, 6, 4]
b = a.copy()
a.append(2)
b.pop()

print(b)


# a- [8, 6, 4] 
# b- [8, 6, 4, 2] 
# c- [6, 4]
# b. [8, 6]


# Explanation:

# a = [8, 6, 4]: This line initializes a list a with elements 8, 6, and 4.
# b = a.copy(): This line creates a shallow copy of list a and assigns it to b. 
# This means that b is a new list object containing the same elements as a but stored at a different memory location.
# a.append(2): This line appends the integer 2 to the end of list a. 
# After this line, a will be [8, 6, 4, 2].
# b.pop(): This line removes and returns the last element from list b. 
# Since b is a copy of a up to this point, it still has the original elements [8, 6, 4]. 
# After popping, b will be [8, 6].

# The correct output is [8, 6]