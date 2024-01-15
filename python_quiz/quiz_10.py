# Python Quiz (10) 😉

# What is the output of this code and why🤔?


def check():

    condition = (True and False) or (" " and "")

    if condition or not condition:
        return "2024 is my year"
    elif not condition:
        return "I will continue to procrastinate"
    else:
        return "I'm just a loser"

print(check())

# Output

# a. "I'm just a loser"
# b. "I will continue to procrastinate"
# c. "2024 is my year"


# Explanation

# - Inside the function, there is a variable called condition. 
# - The value of this variable is determined by the expression (True and False) or (" " and "").
# - In the expression (True and False), the and operator is used to evaluate the logical conjunction between True and False. 
# - Since the result of and operator is False if any of the operands is False, the expression evaluates to False.
# - In the expression (" " and ""), the and operator is used to evaluate the logical conjunction between two empty strings.
# - Since both the strings are considered "truthy" values, the result of the and operator will be the second value, which is an empty string "".
# - Finally, the expression (True and False) or (" " and "") evaluates to False or "", which is equivalent to False.
# - The code then enters an if statement to check the value of the condition variable.
# - The condition condition or not condition is evaluated. 
# - Since the value of condition is False, the not condition part becomes True, resulting in False or True. 
# - The or operator returns True if any of the operands is True, so the condition evaluates to True.
# - The first branch of the if statement is executed because the condition is True. The function returns the string "2024 is my year".
# - The function call print(check()) executes the check() function and prints the returned value to the console.
# - In summary, the code checks the value of the condition variable and returns different messages based on its value.
# - Since the value of condition is False, the function returns the string "2024 is my year".