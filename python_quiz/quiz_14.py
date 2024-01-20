# Python Quiz (14) 😉

# What is the output of this code and why 🤔?


lst = ["Hello", 1, 3, 4, 7, "Dev"]

number_1 = lst.pop(2)
number_2 = lst.pop(3)

print( sum( (number_1, number_2) ) )


# Output:

# a- 5
# b- 7
# c- 10
# d- 6


# Explanation:

# We create a list called lst which contains a mix of strings and numbers: ["Hello", 1, 3, 4, 7, "Dev"].
# Next, we use the pop() method on the lst list to remove two elements from it. 
# The pop() method allows us to remove and retrieve an element from a list based on its index position.
# The first pop(2) call removes the element at index position 2 from lst, which is the number 3.
# This value is then assigned to the variable number_1.
# The second pop(3) call removes the element at index position 3 from the updated lst (after the previous pop() call), which is the number 7.
# This value is assigned to the variable number_2.
# After the above operations, the lst list will be modified and have the elements ["Hello", 1, 4, "Dev"].
# Finally, we use the sum() function to calculate the sum of number_1 and number_2 and then print the result.
# The sum() function takes an iterable (in this case, a tuple containing number_1 and number_2) and returns the sum of its elements.
# In this case, the sum of number_1 (which is 3) and number_2 (which is 7) is 10.
# Therefore, the correct answer is c- 10.

