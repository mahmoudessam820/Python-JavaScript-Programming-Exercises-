"""
    Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

    Debug code 🧐: https://pythontutor.com/python-compiler.html#mode=edit  
"""


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0 
    buy = prices[0]
    
    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell

    return profit 

print(max_profit([7,1,5,3,6,4]))





