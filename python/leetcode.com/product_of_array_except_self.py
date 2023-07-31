"""
    Product of Array Except Self

    - Given an integer array nums, return an array answer such that, 
    - Answer[i] is equal to the product of all the elements of nums except nums[i].
    - The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    - You must write an algorithm that runs in O(n) time and without using the division operation.


    Examples: 

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]


    Task URL: https://leetcode.com/problems/product-of-array-except-self/

"""

def productExceptSelf(nums: list[int]) -> list[int]:

    n = len(nums)
    answer = [0] * n

    # Calculate prefix products
    answer[0] = 1
    for i in range(1, n):
        answer[i] = answer[i-1] * nums[i-1]

    # Calculate suffix products and multiply with prefix products
    suffix = 1
    for i in reversed(range(n)):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

print(productExceptSelf([1,2,3,4]))
