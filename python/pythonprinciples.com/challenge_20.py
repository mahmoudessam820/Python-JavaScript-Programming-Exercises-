"""
    level of challenge 5/10

    Custom zip

    The built-in zip function "zips" two lists. 
    Write your own implementation of this function.

    Define a function named zap. 
    The function takes two parameters, a and b. These are lists.

    Your function should return a list of tuples. 
    Each tuple should contain one item from the a list and one from b.

    You may assume a and b have equal lengths.
    If you don't get it, think of a zipper.

    For example:

    zap(
        [0, 1, 2, 3],
        [5, 6, 7, 8]
    )

    Should return:

    [
        (0, 5),
        (1, 6),
        (2, 7),
        (3, 8)
    ]

    Hint

    Use a while loop or a for loop with range to count up an index i. 
    Then use i to access each element in a and b at a time. 
    Create a tuple and append it to a result list that you gradually build up.

"""

# My solution

def zap(a, b):
    zap_list = []
    for i in range(len(a)): 
        zap_list.append((a[i], b[i]))
    return zap_list

print(zap([0, 1, 2, 3], [5, 6, 7, 8]))


# Another solution

def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result


# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]