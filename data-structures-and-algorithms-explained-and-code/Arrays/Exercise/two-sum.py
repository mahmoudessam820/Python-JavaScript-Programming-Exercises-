"""
    Problem: https://leetcode.com/problems/two-sum/description/

    Debug code 🧐: https://pythontutor.com/python-compiler.html#mode=edit  
"""


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    pre_map: dict = {}

    for i, n in enumerate(nums):

        diff = target - n

        if diff in pre_map:

            return [pre_map[diff], i]

        pre_map[n] = i


print( two_sum([2,7,11,15], 9) )







