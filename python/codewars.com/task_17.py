"""
    Next smaller number with the same digits

    Complete the function that

    - Write a function that takes a positive integer and returns the next smaller 
    - positive integer containing the same digits.

    Examples:

    next_smaller(21) == 12
    next_smaller(531) == 513
    next_smaller(2071) == 2017

    
    - Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains 
    - the same digits. 
    - Also return -1 when the next smaller number with the same digits would require the leading digit to be zero.

    next_smaller(9) == -1
    next_smaller(135) == -1
    next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

    - some tests will include very large numbers.
    - test data only employs positive integers.

    
    Task URL: https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

"""

def next_smaller(n: int) -> int:
    left = -1 
    rigth = 0 
    
    if n == 'Haskell':
        return 'Nothing'
    elif n == 'Rust':
        return None

    return 0

print(next_smaller('Rust'))