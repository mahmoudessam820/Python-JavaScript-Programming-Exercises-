"""

    Credit Card Mask

    - Usually when you buy something, you're asked whether your credit card number,
    - phone number or answer to your most secret question is still correct. 
    - However, since someone could look over your shoulder, 
    - you don't want that shown on your screen. Instead, we mask it.

    - Your task is to write a function maskify, 
    - which changes all but the last four characters into '#'.

    Examples:

    "4556364607935616"      -->  "############5616"
    "64607935616"           -->      "#######5616"
    "1"                     -->                "1"
    ""                      -->                 ""

    "What was the name of your first pet?"

    "Skippy"                                    --> "##ippy"
    "Nananananananananananananananana Batman!"  --> "####################################man!"

    Task URL: https://www.codewars.com/kata/5412509bd436bd33920011bc/python

"""


def maskify(cc):

    credit_card = str(cc)

    if len(credit_card) == 1 or len(credit_card) == 4:
        return credit_card
    if credit_card == "":
        return ""

    start = credit_card[0:-4]
    end = credit_card[-4:]
    hash = len(start) * '#'
    hash_credit_card = "".join([hash, end])

    return hash_credit_card


print(maskify("Skippy"))
