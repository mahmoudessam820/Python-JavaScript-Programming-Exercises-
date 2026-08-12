"""
    Problem: https://leetcode.com/problems/move-zeroes/

    Debug code 🧐: https://pythontutor.com/python-compiler.html#mode=edit  
"""


def move_zeroes(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    # Initialize two pointers
    non_zero_idx = 0

    # Traverse the list
    for i in range(len(nums)):
        # If current element is not zero, swap it with the element at non_zero_idx
        if nums[i] != 0:
            # Swap elements
            nums[non_zero_idx], nums[i] = nums[i], nums[non_zero_idx]
            # Increment non_zero_idx
            non_zero_idx += 1
    
    return nums 
    
print(move_zeroes([0,1,0,3,12]))



