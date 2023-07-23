"""
    Contains Duplicate

    - Given an integer array nums, return true,
    - If any value appears at least twice in the array.
    - And return false if every element is distinct.

    Examples: 

    Input: nums = [1,2,3,1]
    Output: true

    Input: nums = [1,2,3,4]
    Output: false

    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

    Task URL: https://leetcode.com/problems/contains-duplicate

"""


def containsDuplicate(nums: list[int]) -> bool:

    filter_nums: list[int] = [i for i in set(nums)]
    return len(filter_nums) != len(nums)


print(containsDuplicate([1, 2, 3, 1]))
