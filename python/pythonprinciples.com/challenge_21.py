"""
    level of challege 5/10

    Solution validation

    The aim of this challenge is to write code that can analyze code submissions. 
    We'll simplify things a lot to not make this too hard.

    Write a function named validate that takes code represented 
    as a string as its only parameter.

    Your function should check a few things:

    the code must contain the def keyword
        otherwise return "missing def"

    the code must contain the : symbol
        otherwise return "missing :"

    the code must contain ( and ) for the parameter list
        otherwise return "missing paren"

    the code must not contain ()
        otherwise return "missing param"

    the code must contain four spaces for indentation
        otherwise return "missing indent"

    the code must contain validate
        otherwise return "wrong name"

    the code must contain a return statement
        otherwise return "missing return"

    If all these conditions are satisfied, your code should return True.
    Here comes the twist: your solution must return True when validating itself.

    Hint

    You can perform a series of checks like this:

    if "def" not in code:
        return "missing def"

    If you get to the last check, we'll try running your code on your code. 
    If this returns "missing param" it's probably because you have () in your code somewhere, 

    perhaps in a line such as this:

    if "()" in code:
    return "missing param"

    To get past this, find some clever workaround to still check for "()" 
    without using the literal string.

    Task URL: https://pythonprinciples.com/challenges/Solution-validation/

"""

#! My Solution


def validate(code):

    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" not in code or ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    return True
