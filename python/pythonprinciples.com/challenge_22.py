"""
    level of challenge 5/10

    List xor

    Define a function named list_xor.
    Your function should take three parameters: 
    - n, list1 and list2.

    Your function must return whether n is exclusively 
    - In list1 or list2. 

    In other words, if n is in both lists or in none of the lists, 
    return False.
    If n is in only one of the lists, return True.

    For example:

    1- list_xor(1, [1, 2, 3], [4, 5, 6]) == True
    2- list_xor(1, [0, 2, 3], [1, 5, 6]) == True
    3- list_xor(1, [1, 2, 3], [1, 5, 6]) == False
    4- list_xor(1, [0, 0, 0], [4, 5, 6]) == False
    5- list_xor(5, [5, 5, 5], [4, 4, 4]) == True

"""

# My Solution 😊


def list_xor(n, list1, list2):

    list_one = n in list1
    list_tow = n in list2

    if list_one != list_tow:
        return True

    if list_one == list_tow:
        return False


print(list_xor(5, [5, 5, 5], [4, 4, 4]))
