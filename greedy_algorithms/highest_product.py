# Time: O(n)
# Space: O(1)

import math


def highest_product_three(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 integers provided')

    largest_three = [-math.inf, -math.inf, -math.inf]
    smallest_two = [math.inf, math.inf]
    
    for num in list_of_ints:
        largest_three = sorted(largest_three + [num])[1:]
        smallest_two = sorted(smallest_two + [num])[:2]

    product1 = largest_three[0] * largest_three[1] * largest_three[2]
    product2 = smallest_two[0] * smallest_two[1] * largest_three[-1]

    return max(product1, product2)


print(highest_product_three([3, 2, 1, 4, 5])) # 60
print(highest_product_three([4, 2, 0, 1])) # 8
print(highest_product_three([-6, -2, 2, 0, 1])) # 24
print(highest_product_three([-6, -2, -2, 0])) # 0
print(highest_product_three([-6, -2, -2, -1])) # -4
print(highest_product_three([-6, -2])) # -4
