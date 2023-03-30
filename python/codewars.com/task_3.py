'''
    Create Phone Number

    Write a function that accepts an array of 10 integers (between 0 and 9). 
    That returns a string of those numbers in the form of a phone number.

    Example:

    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) 
    # => returns "(123) 456-7890"

    Note:

    The returned format must be correct in order to complete this challenge.
    Don't forget the space after the closing parentheses!

    Task URL: https://www.codewars.com/kata/525f50e3b73515a6db000b83/python

'''


def create_phone_number(phone_number) -> str:

    if isinstance(phone_number, list) and len(phone_number) == 10:

        phone: str = str([number for number in phone_number])
        pn: str = phone.replace(',', "").replace(' ', '')

        return f"({pn[1:4]}) {pn[4:7]}-{pn[7:11]}"
    else:
        return "Something went wrong"


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
