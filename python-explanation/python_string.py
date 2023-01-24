# Python string methods explanation 🐍


# capitalize() 
# method returns a string where the first character is upper case, 
# and the rest is lower case.

txt = "hello world"

x = txt.capitalize()

# output
# Hello world


# casefold() 
# method returns a string where all the characters are lower case.
# This method is similar to the lower() method, but the casefold()
# method is stronger, more aggressive, meaning that it will convert more characters into lower case
# and will find more matches when comparing two strings and both are converted using the casefold() method.

txt = "Hello, And Welcome!"

x = txt.casefold()

# output
# hello, and welcome!


# center() 
# method will center align the string, using a specified character (space is default) as the fill character.

txt = "welcome"

x = txt.center(20, "*")

# output
#   welcome  
#******welcome*******  


# count() 
# method returns the number of times a specified value appears in the string.


txt = "hello, and welcome and hi! "

x = txt.count("and")

# output
# 2


# endswith() 
# method returns True if the string ends with the specified value, otherwise False.

txt = "hello world!"

x = txt.endswith("!")

# output
# True


# find() 
# method finds the first occurrence of the specified value.
# method returns -1 if the value is not found.

# Note: 
# The find() method is almost the same as the index() method, 
# the only difference is that the index() method raises an exception if the value is not found.


txt = "Hello, welcome to python string."

x = txt.find('welcome')

# output
# 7



# format() 
# method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.

txt1 = "Hello, {} to python {}".format("welcome", "string")

txt2 = "Hello, I'm {name} and I'm a {job}".format(name="Mahmoud", job="developer")

txt3 = "My name is {0}, I'm {1}".format("John",36)

# output
# 1 - Hello, welcome to python string
# 2 - Hello, I'm Mahmoud and I'm a developer
# 3 - My name is John, I'm 36



# format_map() 
# method is an inbuilt function in Python, 
# which is used to return a dictionary key’s value.

details = {
    "name": "John",
    "job": "developer"
}

x = "Hi, I'm {name} and I'm a {job}. ".format_map(details)

# output
# Hi, I'm John and I'm a developer. 


# index() 
# method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.

# Note:
# The index() method is almost the same as the find() method
# The only difference is that the find() method returns -1 if the value is not found. 


txt = "hello world!"

x = txt.index("!")

# output
# 11


# isalnum() 
# method returns True if all the characters are alphanumeric 
# meaning alphabet letter (a-z) and numbers (0-9)

txt = "Company12"

x = txt.isalnum()

# output
# True


# isalpha() 
# method returns True if all the characters are alphabet letters (a-z).
# Example of characters that are not alphabet letters: (space)!#%&? etc.

txt = "helloworld"

x = txt.isalpha()

# output
# True


# isdigit() 
# method returns True if all the characters are digits, otherwise False.

txt = "2022"

x = txt.isdigit()

# output
# True


# isidentifier() 
# method returns True if the string is a valid identifier, otherwise False.
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.

txt = "Python"

x = txt.isidentifier()

# output
# True

# islower() 
# method returns True if all the characters are in lower case, otherwise False.
# Numbers, symbols and spaces are not checked, only alphabet characters.

txt = "hello world"

x = txt.islower()

# output
# True


# lstrip() 
# method removes any leading characters (space is the default leading character to remove)

txt = "     Python      "

x = txt.lstrip()

# output
# Welcome to Python       methods explanation


# maketrans() 
# method returns a mapping table that can be used with the translate() method to replace specified characters.

txt = "Delcome to Python"

trans = txt.maketrans("D", "W")

result = txt.translate(trans)

# output
# Welcome to Python


# partition() 
# method searches for a specified string, and splits the string into a tuple containing three elements.
#1- The first element contains the part before the specified string.
#2- The second element contains the specified string.
#3- The third element contains the part after the string.

# Note: This method searches for the first occurrence of the specified string.

txt = "welcome to python methods explanation"

x = txt.partition("python")

# output
# ('welcome to ', 'python', ' methods explanation')



# replace() 
# method replaces a specified phrase with another specified phrase.
# Note: All occurrences of the specified phrase will be replaced 
# if nothing else is specified.


txt = "welcome to python method explanation"

x = txt.replace("python", "replace()")

# output
# welcome to replace() method explanation


# rfind() 
# method finds the last occurrence of the specified value.
# method returns -1 if the value is not found.

txt = "welcome to python method explanation"

x = txt.rfind("explanation")

# output
# 25


# rjust() 
# method will right align the string, using a specified character (space is default) as the fill character.

txt = "hello world"

x = txt.rjust(20)

# output
#          hello world


# split() 
# method splits a string into a list.
# You can specify the separator, default separator is any whitespace.

txt = "hello world"

x = txt.split()

# output
# ['hello', 'world']


# splitlines() 
# method splits a string into a list. The splitting is done at line breaks.

txt = "welcome to python\n method explanation"

x = txt.splitlines()

# output
# ['welcome to python', ' method explanation']


# startswith() 
# method returns True if the string starts with the specified value, otherwise False.

txt = "Hello world"

x = txt.startswith("Hello")

# output
# True


# strip() 
# method removes any leading (spaces at the beginning) and trailing 
# (spaces at the end) characters (space is the default leading character to remove)


txt = "    python      "

x = txt.strip()

# output
# welcome to python method explanation


# swapcase() 
# method returns a string where all the upper case letters are lower case and vice versa.

txt = "Hello My Name Is MAHMOUD"

x = txt.swapcase()

# output
# hELLO mY nAME iS mahmoud


# title() 
# method returns a string where the first character in every word is upper case. Like a header, or a title.
# If the word contains a number or a symbol, the first letter after that will be converted to upper case.

txt = "python method explanation"

x = txt.title()

# output
# Python Method Explanation


# upper() 
# method returns a string where all characters are in upper case.
# Symbols and Numbers are ignored.

txt = "Hello my friends"

x = txt.upper()


# output
# HELLO MY FRIENDS


# zfill()
#  method adds zeros (0) at the beginning of the string, until it reaches the specified length.
# If the value of the len parameter is less than the length of the string, no filling is done.

txt = "50"

x = txt.zfill(10)

# output
# 0000000050


# Note: All string methods returns new values. 
# They do not change the original string.