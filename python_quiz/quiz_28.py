# Python Quiz (28) 😉

# What is the output of this code and why🤔?


def outer_func(y):
    x = 2 

    def inner_func():
        return x + y 

    x = x + 2 
    y = 2 
    return inner_func 

results = outer_func(3)

print(results())


# Output 

# a- 7
# b- 6
# c- 5
# d- 4


# Explanation:

# outer_func(y) is defined with a parameter y
# Inside outer_func, x is initialized to 2
# inner_func is defined inside outer_func This inner function returns the sum of x and y
# x is modified to x + 2, which makes x equal to 4
# y is modified to 2
# outer_func returns the inner_func function object
# print(results()) calls the inner_func returned by outer_func
# Inside inner_func, x is 4 and y is 2 due to the modifications inside outer_func
# inner_func returns x + y, which is 4 + 2 = 6

# So the correct answer is b- 6 😉