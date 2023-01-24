'''
    Split Strings

    Complete the solution so that it splits the string 
    Into pairs of two characters.

    If the string contains an odd number of characters then 
    It should replace the missing second character of 
    The final pair with an underscore ('_').

    Examples:

    solution('abc')  should return => ['ab', 'c_']
    solution('abcdef') should return => ['ab', 'cd', 'ef']

    Task URI: https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

'''

def solution(s):
    step = 2
    if len(s) % 2 == 0:
        return  [s[index : index + step] for index in range(0, len(s), step)]
    else:
        odd_str = [s[index : index + step] for index in range(0, len(s), step)] 
        el = odd_str[-1] + '_'
        odd_str.pop()
        odd_str.append(el)
        return odd_str


print(solution('amr'))

