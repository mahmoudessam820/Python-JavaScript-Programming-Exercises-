"""
    level of challenge 4/10

    Palindrome

    A string is a palindrome when it is the same 
    when read backwards.

    For example:
    the string "bob" is a palindrome So is "abba".
    But the string "abcd" is not a palindrome, because "abcd" != "dcba".

    Write a function named palindrome that takes a single string as its parameter.
    Your function should return True if the string is a palindrome, and False otherwise.


"""

# My solution

def palindrome(string):
    pal_string = list( string.casefold() )
    rev_string = list( reversed(pal_string) )

    if pal_string == rev_string:
        return True
    else:
        return False

print(palindrome("aba"))



# Another solution

def palindrome(string):
    while len(string) > 1:
      head = string[0]
      tail = string[-1]
      string = string[1:-1]
      if head != tail:
        return False
    return True


# recursive solution: equivalent to the above.
def palindrome(string):
  if len(string) < 2:
    return True
  return string[0] == string[-1] and palindrome(string[1:-1])


# check if reversing the string gives the same string.
def palindrome(string):
  return string == string[::-1]
