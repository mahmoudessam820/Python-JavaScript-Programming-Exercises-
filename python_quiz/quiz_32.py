# Python Quiz (32) 😉
# What is the output of this code and why🤔?

x = 3
y = 4
z = 5

print(x if not x + y * z else y)


# Output

# a. 3
# b. 4
# c. 23
# d. False
# e. True


# Explanation:

# Understand the variables: The code initializes x = 3, y = 4, and z = 5.

# Analyze the ternary operator: The expression x if not x + y * z else y follows the structure true_value if condition else false_value.

# Here, x (3) is returned if the condition not x + y * z is True; otherwise, y (4) is returned.

# First, evaluate y * z: Since multiplication has higher precedence than addition, calculate 4 * 5 = 20.

# Then, compute x + y * z: 3 + 20 = 23.

# Apply the not operator: In Python, non-zero numbers are True in a boolean context, so 23 is True, and not 23 is not True, which is False.

# Evaluate the ternary operator: Since the condition not x + y * z is False, the expression returns y, which is 4.

# The correct answer is: 4 option b