"""
    level of challenge = 2/10

    Middle letter

    - Write a function named mid that takes a string as its parameter. 
    - Your function should extract and return the middle letter. 
    - If there is no middle letter, your function should return the empty string.
    - For example, mid("abc") should return "b" and mid("aaaa") should return "".

    Hint

    - First check if the string's length is even, and if so, return "". 
    - You can use the % (modulo) operator to check. 
    - An even string's length modulo 2 is 0, while an odd string's length modulo 2 is 1. 
    - You can google "python check if number is even or odd" for clarification.
    - Also, note that in Python, an index must be an integer, not a floating-point number. So 2 is a valid index, but 2.0 is not. 
    - Therefore use integer division // to calculate the index, or cast the float to an integer with int().

"""

# My solution 

def mid(my_string):
    length = len(my_string) % 2
    if length == 0:
        return ""
    elif length != 0:
        middle = len(my_string) // 2
        return my_string[middle]
print(mid("cars"))

# The another soultion 

# this approach uses // which is integer division in Python 3
# alternatively, use / and int() in combination.
def middel(string):
    if len(string) % 2 == 0:
        return ""
    return string[len(string)//2]
print(middel("abc"))


