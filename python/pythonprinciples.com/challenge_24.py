"""
    level of challenge 7/10

    Thousands separator

    Write a function named format_number that takes 
    A non-negative number as its only parameter.

    Your function should convert the number to a string and 
    Add commas as a thousands separator.

    For example: 
    calling format_number(1000000) should return "1,000,000".

    Hint:
    Convert the number to a string and iterate over each digit.
    Iterate backwards, or start by reversing the string 
    to make your life easier.

"""

def format_number(number):
    return ("{:,}".format(number))
print(format_number(1000000))