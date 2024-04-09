# Python Quiz (21) 😉
# What is the output of this code and why🤔?



fun_lambda = lambda x: ( lambda y:(lambda z: z) )

result = fun_lambda(10)(20)(30)

print(result)


#Output

# a- 60
# b- 20
# c- 30
# d- 10


# Explanation:

# fun_lambda = lambda x: ( lambda y:(lambda z: z) )

# This line defines a lambda function called fun_lambda.
# It takes a single argument x.
#  Inside fun_lambda, there's another lambda function that takes a single argument y, and inside that, there's yet another lambda function that takes a single argument z and returns it.
# So essentially, fun_lambda returns a function that takes y, which in turn returns a function that takes z and returns it.

# result = fun_lambda(10)(20)(30)

# Here, you're calling fun_lambda with the argument 10, which returns a function that expects y.
# You then immediately call this function with 20, which returns another function that expects z. 
# Finally, you call this last function with 30.
# Since the innermost lambda function just returns z, the value of z is 30, which is the result of this chain of function calls.

# So, the correct output is: c- 30