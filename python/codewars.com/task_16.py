"""
    Merged String Checker

    At a job interview, you are challenged to write an algorithm to check if a given string,
    s, can be formed from two other strings, part1 and part2.
    The restriction is that the characters in part1 and part2 should be in the same order as in s.
    The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

    For example:

    'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
    part1:  c   d   w         = cdw
    part2:    o   e   a r s   = oears


    Task URL: https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

"""


def is_merge(s, part1, part2):

    text = part1 + part2 
    index1 = 0
    index2 = 0

    if len(text) != len(s): return False

    for char in s:
        if index1 < len(part1) and char == part1[index1]: 
            index1 += 1 
        elif index2 < len(part2) and char == part2[index2]:
            index2 += 1

    return index1 == len(part1) and index2 == len(part2) 

print(is_merge('codewars', 'cdw', 'oears'))