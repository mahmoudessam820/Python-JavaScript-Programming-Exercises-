# Python Quiz (12) 😉

# What is the output of this code and why🤔?


empty, first_new, last_new = "", "Guido", "Van Rossum"

results = empty or first_new or last_new 

print(results)


# Output 

# a. ""
# b. "Guido"
# c. "Van Rossum"
# d. Error 

# Explanation  

# we have three variables: empty, first_new, and last_new.
# The empty variable is assigned an empty string "", while first_new is assigned the string "Guido", and last_new is assigned the string "Van Rossum".
# Next, we create a new variable called results and assign it a value based on the logical operation between these variables.
# In Python, the or operator returns the first truthy value it encounters, or the last value if all are falsy.
# In this case, since empty is falsy, Python moves on to check first_new. 
# Since first_new is truthy as it contains a non-empty string, Python stops evaluating further and assigns the value of first_new to results.
# Finally, we print the value of results, which in this case will be the string "Guido".
# Therefore, the output of the code will be: b. "Guido"
