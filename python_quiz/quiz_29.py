# Python Quiz (29) 😉
# What is the output of this code and why🤔?

count = 0

def increment():
    count += 1
    return count

print(increment())


# Output

# a. 1
# b. 0
# c. SyntaxError
# d. UnboundLocalError


# Explanation: 

# - count is assigned 0 at the global scope.
# - The function increment() tries to do count += 1 without declaring count as global inside the function.
# - In Python, if you assign to a variable inside a function, Python treats that variable as local to that function scope unless you declare it as global.
# - So, when Python executes count += 1, it's actually translated to:
#     count = count + 1
# - But, at this point, local count has not been defined or initialized, so Python raises an UnboundLocalError.

# The correct answer is: d. UnboundLocalError