# Python Quiz (30) 😉
# What is the output of this code and why🤔?


def func(lst):
    lst.pop(0)
    lst.append(lst[1])
    return lst if lst.count("Dil") > 1 else ...


names = ['Kil', 'Pil', 'Dil', 'Sil']

print(func(names))


# Output

# a. Ellipsis
# b. ['kil', 'Pil', 'Dil', 'Sil']
# c. ['Pil', 'Dil', 'Sil', 'Dil']
# d. Error


# Explanation:

# The list names initially ['Kil', 'Pil', 'Dil', 'Sil']

# lst.pop(0) removes the first element ('Kil'). 

# Now the list is ['Pil', 'Dil', 'Sil'].

# lst.append(lst[1]) appends the second element ('Dil') to the end of the list. 

# Now the list is ['Pil', 'Dil', 'Sil', 'Dil'].

# The condition lst.count("Dil") > 1 checks how many times "Dil" appears. 

# It appears twice, so the condition is true.

# Since the condition is true, the function returns the modified list ['Pil', 'Dil', 'Sil', 'Dil'].

# The correct answer is: c. ['Pil', 'Dil', 'Sil', 'Dil']