# Python Quiz (18) 😉
# What is the output of this code and why 🤔?

data = [ ["Hi", "Python"] ]

print( "Yes"  if 'hi' in data[0][0] else data[0][1] )


# Output 

# a- "hi"
# b- "Python"
# c- True 
# d- "Yes"


# Explanation 

# data = [["Hi", "Python"]] This line initializes a list called data with one nested list ["Hi", "Python"].
# This nested list contains two elements the string "Hi" at index 0 and the string "Python" at index 1.
# print("Yes" if 'hi' in data[0][0] else data[0][1]) This line contains a conditional expression.
# 'hi' in data[0][0] This checks if the substring 'hi' is present in the string "Hi" which is at index 0 of the first element of data, Note that the comparison is case-sensitive. 
# Since 'hi' is not exactly present in "Hi", this expression evaluates to False.
# The second part of the conditional expression (data[0][1]) would be executed. 
# This part retrieves the element at index 1 of the first element of data, which is "Python", and this would be printed.

# Therefore, the correct answer is: b- "Python"