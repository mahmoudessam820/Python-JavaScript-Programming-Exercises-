# Python Quiz (13) 😉

# What is the output of this code and why🤔?


best_language = {"name": "python"}

print(best_language.values() == best_language.values())


# Output

# a. True
# b. False
# c. Error
# d. None


# Explanation 

# First, a dictionary called best_language is initialized with a single key-value pair.
# The key is "name" and the corresponding value is "python".
# The values() method is called on the best_language dictionary.
# This method returns a view object containing all the values in the dictionary. 
# In this case, it will return a view object with a single value, which is "python".
# The == operator is used to compare the values returned by calling values() on best_language with itself. 
# In this case, the comparison is done with an exact copy of the same view object. 
# Since the view objects are not the same object in memory, the comparison evaluates to False.
# So, the correct output for this code is indeed False.