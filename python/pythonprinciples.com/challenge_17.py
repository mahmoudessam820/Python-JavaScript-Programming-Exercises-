"""
    level of challenge 4/10

    All equal

    Define a function named all_equal 
    that takes a list and checks whether all elements in 
    the list are the same.

    For example: 
    calling all_equal([1, 1, 1]) should return True.

"""
# My solution

def all_equal(equal_list):

    result = all(element == equal_list[0] for element in equal_list)

    if (result):
        return True
    else:
        return False

print(all_equal([1, 1, 1]))


# Aother solution 

def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True
