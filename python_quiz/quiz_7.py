# Python Quiz (7)😉

# What is the output of this code and why 🤔?


a = []
b = 2

print(a or b)

# Output

# a- True
# b- False
# c- 2
# d- [] 


# The output of the code will be (2)

# Explanation

# In Python, the OR operator returns the first truthy value it encounters when evaluating a sequence of expressions. 

# Here's how it works in your code:

# 1- a is an empty list, which is considered "falsy" in Python.
# 2- b is equal to 2, which is considered "truthy" in Python.

# When you use the OR operator, it will return the first "truthy" value it encounters.

# In this case, it's b because a is "falsy." 
# So, the expression a OR b evaluates to b, which is 2. 
# Therefore, the code prints 2.