"""

    Exes and Ohs

    Check to see if a string has the same amount of 'x's and 'o's. 
    The method must return a boolean and be case insensitive.
    The string can contain any char.

    Examples input/output:

    XO("ooxx")      => true
    XO("xooxx")     => false
    XO("ooxXm")     => true
    XO("zpzpzpp")   => true // when no 'x' and 'o' is present should return true
    XO("zzoo")      => false

    
    Task URL: https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
    
"""


def xo(s: str):

    to_lower_case: any = s.lower()

    character_list: list[str] = list(map(str, to_lower_case))
    xo_list: list[str] = ['x', 'o']

    x: int = 0
    o: int = 0

    filter_list: list[str] = list(
        filter(lambda x: x in xo_list, character_list))

    for char in filter_list:
        if char == 'x':
            x += 1
        elif char == 'o':
            o += 1

    if x != o and filter_list != []:
        return False
    elif filter_list != [] or filter_list == []:
        return True


print(xo("zzoo"))
