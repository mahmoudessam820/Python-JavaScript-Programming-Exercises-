"""
  Palindrome Number

  Given an integer x, return true if x is palindrome integer.

  An integer is a palindrome when it reads the same backward as 
  forward. For example, 121 is palindrome while 123 is not.


  Example 1:
  Input: x = 121
  Output: true

  Example 2:

  Input: x = -121
  Output: false

  Explanation: 
  
  From left to right, it reads -121.
  From right to left, it becomes 121-. 
  Therefore it is not a palindrome.

  leetcode Task URL: https://bit.ly/3Prd3bK

"""

# My Solution

def isPalindrome(x):
    pal_num = str(x)

    while len(pal_num) > 1:
        head = pal_num[0]
        tail = pal_num[-1]
        pal_num = pal_num[1:-1]

        if head != tail:
            return False

    return True


print(isPalindrome(121))
