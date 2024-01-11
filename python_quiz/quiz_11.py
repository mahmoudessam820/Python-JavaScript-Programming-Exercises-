# Python Quiz (11) 😉

# What is the output of this code and why🤔?


lst = [10, 23, 25, 45, 10],

print(lst[:].count(10))


# Output

# a. 0
# b. 1
# c. 2
# d. Error


# Explanation

# lst = [10, 23, 25, 45, 10],: This line declares a variable named lst and assigns it a list of integers [10, 23, 25, 45, 10]. 
# It is important to note that there is an extra comma at the end, which creates a tuple with a single element.
# So, lst is actually a tuple containing a single list.
# The trailing comma after the list causes lst to be assigned as a tuple containing a single element, which is the list itself.
# As a result, when the count() method is called on lst, it is treating the entire list as one element and not finding any instances of 10.
# So, the output is 0.