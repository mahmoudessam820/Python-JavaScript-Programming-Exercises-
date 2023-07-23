"""
    Top K Frequent Elements

    - Given an integer array nums and an integer k. 
    - Return the k most frequent elements.
    - You may return the answer in any order.

    Examples:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

    Input: nums = [1], k = 1
    Output: [1]

    Task URL: https://leetcode.com/problems/top-k-frequent-elements/

"""


def topKFrequent(nums: list[int], k: int) -> list[int]:

    # Create a dictionary to store the frequency of each element in 'nums'
    freqs = {}

    # Loop through the 'nums' list to calculate the frequency of each element
    for element in nums:

        if element in freqs:
            freqs[element] += 1 # If element already exists in 'freqs', increment its count

        else:
            freqs[element] = 1 # If element does not exist in 'freqs', initialize its count to 1


    # Sort the dictionary 'freqs' based on the frequency of elements in descending order
    sorted_keys = dict(sorted(freqs.items(),
                                    key=lambda x: x[1], reverse=True))

    # Extract the keys elements from the sorted dictionary, representing the most frequent elements
    most_frequent = [x for x in sorted_keys.keys()]


    # Return the 'k' most frequent elements
    return most_frequent[:k]


print(topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
