# Python Quiz (4) 😉

# What is the output of this code and why 🤔?


list_nums = [4, 3, 2, 1]

sorted_list = list_nums.sort()

no_value = None if all(list_nums) else list_nums

print(sorted_list == no_value)


# Output

# a- None
# b- True
# c- False
# d- Error 

# Explanation

# - List of integers named list_nums with four elements in descending order.
# - The sort() method is called on the list, which sorts the list in ascending order.
# - However, it's important to note that the sort() method returns None. 
# - Therefore, the sorted list is not assigned to a new variable but rather replaces the original list so that list_nums now contains [1, 2, 3, 4].
# - The next line checks if all the elements of the list_nums are truthy (non-zero), and if yes,
# - It assigns list_nums to the no_value variable otherwise, None is assigned to no_value.
# - The built-in all() function if all elements are truthy, then all() returns True. 
# - Otherwise, it returns False in this case, the if statement checks if all(list_nums) evaluates to True or False.