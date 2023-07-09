# Python Quiz (1)

# What is the output of this code and why?

a = [7]
p = [7]
a = a * 2

print((a == p.extend(p)))

# Output

# a. True
# b. False
# c. Error
# d. [7, 7]

# The correct answer is b

# The code returns False because the extend() method of a list returns None, and modifies the original list in place.

# 1 - a = [7]: a is assigned a list containing the integer 7.
# 2 - p = [7]: p is assigned a list containing the integer 7.
# 3 - a = a * 2: The * operator is used to multiply the list a by 2, resulting in the list[7, 7]. This new list is assigned to the variable a.
# 4 - p.extend(p) extends the list p with itself, resulting in the list[7, 7].
# 5 - (a == p.extend(p)) compares the list a with the result of invoking extend() on p, which modifies p in place and returns None.
# - Since None is not equal to[1, 1], the expression evaluates to False.
