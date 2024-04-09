# Python Quiz (23) 😉
# What is the output of this code and why🤔?


x = 3
y = 4
z = 5

print(x if not x + y * z else y)


#Output

# a- 3
# b- 4 
# c- 23
# d- False
# e- True


# Explanation:

# The expression x if not x + y * z else y is a conditional expression.
# It evaluates to x if the condition not x + y * z is true (evaluates to True), otherwise it evaluates to y.
# y * z evaluates to 20.
# x + y * z evaluates to 3 + 20 = 23.
# not x + y * z evaluates to not 23, which evaluates to False.
# Since the condition evaluates to False, the expression evaluates to y, which is 4.

# So, the output is: b- 4