# Python Quiz (2)

# What is the output of this code and why?


def func(x):

    if x <= 1:
        return 1
    else:
        return x * func(x - 1)


print(func(4))

# Output:

# a- 24
# b- 3
# c- 4
# d- 12

# Answer: 24

# Explanation:

# The function func(x) is called 4 times.

# The func function is a recursive function that calculates the factorial of the input x.

# When x is less than or equal to 1, it returns 1. Otherwise, it multiplies x with the result of calling func with x-1.

# In the example given, func(4) is called which will result in 4 * func(3).

# Then func(3) results in 3 * func(2). Further, func(2) results in 2 * func(1). Finally, func(1) returns 1.

# So we have func(4) = 4 * 3 * 2 * 1 = 24.
