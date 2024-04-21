# Python Quiz (24) 😉
# What is the output of this code and why🤔?


def add_one(x):
    return x + 1


d = {'a': 1, 'b:': 2, 'c': 3}

result = map( add_one, d.values() )
print( list( result ) )

# Output

# a- [2, 3, 4]
# b- (2, 3, 4)
# c- [1, 2, 3]
# d- [2, 3]



# Explanation:


# This defines a function add_one() that takes a single argument x and returns x + 1, effectively incrementing the input by 1.
# This initializes a dictionary d with keys 'a', 'b', and 'c', each mapped to the respective integer values 1, 2, and 3.
# The map() function applies the add_one() function to each value in the dictionary d. 
# d.values() extracts the values from the dictionary ([1, 2, 3]), and map() applies add_one() to each value.
# However, map() returns an iterator in Python 3.x, so it is wrapped in list() to convert it into a list.
# This converts the result of map() to a list and prints it.
# Each value from d.values() has add_one() applied to it, so the output will be [2, 3, 4].

#  The correct output is: a- [2, 3, 4]