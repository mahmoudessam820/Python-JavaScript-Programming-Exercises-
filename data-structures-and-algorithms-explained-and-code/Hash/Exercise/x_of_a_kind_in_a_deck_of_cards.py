"""
    Problem: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

    Debug code 🧐: https://pythontutor.com/python-compiler.html#mode=edit  
"""


def has_groups_sizeX(deck: int):
    """
    :type deck: List[int]
    :rtype: bool
    """
    # Count the frequency of each card
    freq = {}

    for card in deck:
        if card in freq:
            freq[card] += 1
        else:
            freq[card] = 1

    # Function to compute GCD using Euclidean Algorithm
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # Compute GCD of all frequencies
    g = 0
    for count in freq.values():
        g = gcd(g, count)

    return g >= 2
    
print(has_groups_sizeX([1,2,3,4,4,3,2,1,]))