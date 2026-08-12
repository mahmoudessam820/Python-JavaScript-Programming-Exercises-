"""
    Problem: https://leetcode.com/problems/product-of-array-except-self/

    Debug code 🧐: 
    - https://pythontutor.com/python-compiler.html#mode=edit  
    - https://staying.fun/en/
"""




def product_except_self(nums: list[int]):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

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

print(product_except_self([1,2,3,4]))
