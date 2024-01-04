# Python Quiz (9) 😉

# What is the output of this code and why🤔?


my_str = ""
not_str = not my_str
my_bool = True or False  

print(my_bool == not_str)

# Output

# a. False 
# b. True
# c. my_bool
# d. not_str

# Explanation

# -  we start by declaring a variable called my_str and assigning an empty string to it using double quotation marks: my_str = "".
# -  we have another variable called not_str, which is assigned the result of the not operator applied to my_str. 
# -  The not operator is used to negate a boolean value.
# -  In this case, since my_str is an empty string (which evaluates to False in Python), not my_str will be True.
# -  So, not_str will be True.
# -  we have another variable called my_bool, which is assigned the result of the logical OR operator (or) applied to True and False.
# -  The or operator returns True if at least one of the operands is True, otherwise it returns False.
# -  Since True is one of the operands, the result of True or False will be True.
# -  Therefore, my_bool will be True.
# -  Finally, we print the result of the comparison between my_bool and not_str using the equality operator (==). 
# -  The equality operator checks if the two operands are equal. In this case, my_bool is True and not_str is also True, so the expression my_bool == not_str evaluates to True.
# -  So, the output is True.