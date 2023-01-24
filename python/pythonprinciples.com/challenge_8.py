"""
    level of challenge 3/10

    Anagrams

    - Two strings are anagrams 
    - if you can make one from the other by rearranging the letters.
    - Write a function 
    - named is_anagram that takes two strings as its parameters.
    - Your function should return True if the strings are anagrams, 
    - and False otherwise.

    - For example, 
    - the call is_anagram("typhoon", "opython") should return True while the call 
    - is_anagram("Alice", "Bob") should return False.

    Hint

    - You can compare how many times each letter appears in each string.
    - Alternatively, sorting the letters in each string makes this much easier.

"""

# My solution 
def is_anagram(string_one, string_two):
    str_dic_one = {}
    str_dic_tow = {}

    for str_one in string_one:
        if str_one in str_dic_one:
            str_dic_one[str_one] += 1
        else:
            str_dic_one[str_one] = 1

    for str_tow in string_two:
        if str_tow in str_dic_tow:
            str_dic_tow[str_tow] += 1
        else:
            str_dic_tow[str_tow] = 1

    if str_dic_one == str_dic_tow:
        return True
    else:
        return False

print(is_anagram('typhoon', 'opython'))


# Another soultion

# easy solution
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)

# harder solution:
# count how many times each letter appears in each string,
# and make sure all the counts are the same.

def count_letters(string):
    return {l: string.count(l) for l in string}

def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)