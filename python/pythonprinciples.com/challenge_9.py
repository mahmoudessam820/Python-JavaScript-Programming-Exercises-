"""
    level of challenge = 3/10

    Counting syllables

    - Define a function named count that takes a single parameter.
    - The parameter is a string. 
    - The string will contain a single word divided into syllables by hyphens, 
    - Such as these:
        "ho-tel"
        "cat"
        "met-a-phon"
        "ter-min-a-tor"

    - Your function should count the number of syllables and return it.
    - For example, the call count("ho-tel") should return 2.

    Hint:

    The trick is to realize that the number of syllables is the number of times the - symbol appears, plus one.
    You'll have to count hyphens, then. Use a loop to iterate over each letter, or use the .count() method.

"""

# My solution

def count(word):
    new_word = word
    count_syllables = new_word.split('-')
    return len(count_syllables)
print(count("ho-tel"))


# Another solution

def count(word):
    syllables = 1
    for letter in word:
        if letter == "-":
            syllables = syllables + 1
    return syllables

# using the count method
def count(word):
    return word.count("-") + 1

# using split
def count(word):
    return len(word.split("-"))