"""
    level of challenge = 3/10

    Double letters

    The goal of this challenge is to analyze a string to check if it 
    contains two of the same letter in a row. 
    For example, the string "hello" has l twice in a row, 
    while the string "nono" does not have two identical letters in a row.

    Define a function named double_letters that takes a single parameter 
    The parameter is a string. 
    Your function must return True if there are two identical letters 
    in a row in the string, and False otherwise.


    Hint

    Use a for or while loop and keep track of the current index. 
    In each iteration, grab the letter at the current index, 
    And the letter after that, and compare the two.

"""


# My solution

def double_letters(letters):
    for letter in range(len(letters)-1):
        if letters[letter] == letters[letter+1]:
            return True
    return False

print(double_letters("letters"))


# Another soultion

def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False


# shorter solution
# using a list comprehension, zip, and any
def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])])


def has_double_letters(letters):

    for letter in range(len(letters)-1):
        if letters[letter] == letters[letter+1]:
            print(f"There were tow {letters[letter]} at postion {str(letter)}")

print(double_letters("nono"))
