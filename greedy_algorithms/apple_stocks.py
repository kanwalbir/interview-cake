# Time: O(n)
# Space: O(1)

import math


def get_max_profit(stock_prices):
    
    if len(stock_prices) < 2:
        raise ValueError("Less than 2 prices provided")
    
    prev_smallest_price = math.inf  # float("inf")
    profit = -math.inf  # float("-inf")

    for i in range(1, len(stock_prices)):
        prev_smallest_price = min(stock_prices[i-1], prev_smallest_price)
        profit = max(stock_prices[i]-prev_smallest_price, profit)

    return profit


print(get_max_profit([10, 7, 5, 8, 11, 9]))
print(get_max_profit([100, 90, 80, 70, 50, 45]))
print(get_max_profit([0, 0]))
print(get_max_profit([1, 1, 1, 1]))
print(get_max_profit([100]))
print(get_max_profit([0]))
