"""
    Problem: https://leetcode.com/problems/missing-number/

    Debug code 🧐: https://pythontutor.com/python-compiler.html#mode=edit  
"""


def missing_numbe_1(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: int
    """

    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum
    

print(missing_numbe_1([9,6,4,2,3,5,7,0,1]))



def missing_number_2(nums: list[int]) -> int:
    
    missing = len(nums) # Start with 'n' because the loop below only goes up to n-1
    
    for i, num in enumerate(nums):
        missing ^= i ^ num
    
    return missing

print(missing_number_2([9,6,4,2,3,5,7,0,1]))

