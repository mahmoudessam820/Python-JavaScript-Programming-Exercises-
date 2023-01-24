""" 
    level of challenge = 2/10

    Capital indexes

    - Write a function named capital_indexes. 
    - The function takes a single parameter, which is a string. 
    - Your function should return a list of all the indexes in the string that have capital letters.

    - For example, calling capital_indexes("HeLlO") 
    - should return the list [0, 2, 4].

    Hint

    - Your code should consider each letter in the string at a time. 
    - Keep track of the current index; you can do this with enumerate() or manually. 
    - To check if a letter is uppercase, you can use the .isupper() method, 
    - or use the in operator to see if the letter is in "ABCD..XYZ".

"""

# My solution
def capital_indexes(word):
    char_list = []
    for index, char in enumerate(word):
        if char.isupper():
            char_list.append(index) 
    return char_list
print(capital_indexes("HeLlO"))

# Another solution 
# naive solution
def capital_indexes(s):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for i, l in enumerate(s):
        if l in upper:
            result.append(i)
    return result

print(capital_indexes("TiTo"))
# shorter version
from string import uppercase
def capital_indexes(s):
    return [i for i in range(len(s)) if s[i] in uppercase]

# you can also use the .isupper() string method.
