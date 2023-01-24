'''
    Valid Braces

    Write a function that takes a string of braces, and determines if the order of the braces is valid. 
    It should return true if the string is valid, and false if it's invalid.

    All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

    What is considered Valid?

    A string of braces is considered valid if all braces are matched with the correct brace.

    Examples:

    "(){}[]"   =>  True
    "([{}])"   =>  True
    "(}"       =>  False
    "[(])"     =>  False
    "[({})](]" =>  False

    Task URI: https://www.codewars.com/kata/5277c8a221e209d3f6000b56

'''
def validBraces(string):
	brackets = ['()', '{}', '[]']
	while any(x in string for x in brackets):
		for br in brackets:
			string = string.replace(br, '')
	return not string

print(validBraces("(){}[]"))


def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  