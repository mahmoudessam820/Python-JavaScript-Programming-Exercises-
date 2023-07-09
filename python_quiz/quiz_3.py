# Python Quiz (3)

# What is the output of this code and why 😉🤔?

def a(x):
    return 6 + x


def b(x):
    return 2 * x


def c(x):
    return 1 - x


print(
    c(
        b(
            a(3)
        )
    )
)


# Output:

# a- 17
# b- 11
# c- -17
# d- 9

# Answer: -17

# Explanation:

# 1- This is because the functions are being called in reverse order starting with a(3) which returns 9
# 2- That value is passed into b() which multiplies it by 2 to return 18.
# 3- Finally, 18 is passed into c() which subtracts it from 1, returning -17.
# 4- Therefore, c(b(a(3))) evaluates to -17.
