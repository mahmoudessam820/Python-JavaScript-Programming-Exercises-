'''
    Convert string to camel case

    - Complete the method/function so that it converts dash/underscore 
    - Delimited words into camel casing.
    - The first word within the output should be capitalized only if the original 
    - word was capitalized 
    (known as Upper Camel Case, also often referred to as Pascal case).

    Examples:

    "the-stealth-warrior" gets converted to "theStealthWarrior"
    "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

    Task URL: https://www.codewars.com/kata/517abf86da9663f1d2000003

'''


def to_camel_case(text: str) -> str:

    if len(text) > 1:

        if not text[0].isupper():

            case_one: str = ''.join(x for x in text.title() if x.isalnum())
            return case_one[0].lower() + case_one[1:]

        elif text[0].isupper():

            case_tow: str = ''.join(x for x in text.title() if x.isalnum())
            return case_tow

    else:
        return ''


print(to_camel_case('The-Stealth-Warrior'))
