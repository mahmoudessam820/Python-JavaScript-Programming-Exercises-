"""
    Two Sum

    Given an array of integers nums and an integer target, 
    Return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, 
    And you may not use the same element twice.

    You can return the answer in any order.


    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    Task URL: https://leetcode.com/problems/two-sum

"""

def tow_sum(nums, target):
    pre_map = {}

    for i, n in enumerate(nums):
        diff = target - n

        if diff in pre_map:
            return [pre_map[diff], i]

        pre_map[n] = i

print(tow_sum([2, 10, 7, 11, 15], 9))
