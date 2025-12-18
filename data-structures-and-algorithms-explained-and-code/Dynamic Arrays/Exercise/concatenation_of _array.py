"""
    
    Problem: https://leetcode.com/problems/concatenation-of-array/description/

    Idea map 🗺:
    
    - The problem "Concatenation of Array" (LeetCode 1929) asks you to return the array formed by concatenating the input array with itself. 
    - For example, if nums = [1, 2, 3], the output should be [1, 2, 3, 1, 2, 3].
    
    Hint 💡:
    
    - What is the relationship between the input array's length and the output array's length? 
    - How can you use the input array to populate the output array twice?
    - Try writing out the indices for a small example (e.g., nums = [1, 2]) to see the pattern.

    Visual code 🧐: https://pythontutor.com/python-compiler.html#mode=edit  
    
"""


def get_concatenation(nums: int):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    lst = []
    
    for i in nums:
        lst.append(i)

    return nums + lst

print(get_concatenation([1,2,1]))
    