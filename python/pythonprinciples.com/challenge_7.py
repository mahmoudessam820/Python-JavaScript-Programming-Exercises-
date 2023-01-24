"""
level of challenge = 3/10

Adding and removing dots

- Write a function named add_dots that takes a string and adds "." in between each letter. 
- For example
- calling add_dots("test") should return the string "t.e.s.t".

- Then, below the add_dots function, 
- write another function named remove_dots that removes all dots from a string.
- For example
- calling remove_dots("t.e.s.t") should return "test".

- If both functions are correct,
- calling remove_dots(add_dots(string)) should return back the original string for any string.

Hint

- For add_dots you may find the string join method useful.
- If you don't want to use it, 
- You can instead iterate over each letter in, 
- The input while building up a result string that is initially empty.

- The remove_dots function is similar. 
- Either use the string replace method or manually loop over the letters, 
- keeping ones that aren't ".".

"""
# My solution

def add_dots(string):
    new_string = ".".join(string)
    return new_string
print(add_dots("test"))

def remove_dots(string):
    new_string = string
    result = new_string.replace(".", "")
    return result
print(remove_dots("t.e.s.t"))

# Use the remove function and add function togother. 
print(remove_dots(add_dots("tito")))


# Another soultion

# the longer way
def add_dots(s):
    out = ""
    for letter in s:
        out += letter + "."
    return out[:-1] # -> do not show the lest dot 

def remove_dots(s):
    out = ""
    for letter in s:
        if letter != ".":
            out += letter
    return out


# the short way
def add_dots(s):
    return ".".join(s)

def remove_dots(s):
    return s.replace(".", "")