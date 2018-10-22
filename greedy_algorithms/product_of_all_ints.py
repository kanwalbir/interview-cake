# Time: O(n)
# Space: O(n)


def get_products_of_all_ints_except_at_index(int_list):

    lt = len(int_list)
    if lt < 2:
        raise ValueError('Input list must contain atleast 2 elements')

    products = []
    left_product = right_product = 1

    for i in range(0, lt):
        products.append(left_product)
        left_product *= int_list[i]

    for i in range(lt-1, -1, -1):
        products[i] *= right_product
        right_product *= int_list[i]

    return products


print(get_products_of_all_ints_except_at_index([1, 2, 3, 4]))  # [24, 12, 8, 6]
print(get_products_of_all_ints_except_at_index([50, 0, 10]))  # [0, 500, 0]
print(get_products_of_all_ints_except_at_index([-10, 3, -6, -5]))  # [90, -300, 150, 180]
print(get_products_of_all_ints_except_at_index([-10, 3, 0, -5]))  # [0, 0, 150, 0]
print(get_products_of_all_ints_except_at_index([-10, 0, 0, 10]))  # [0, 0, 0, 0]
print(get_products_of_all_ints_except_at_index([]))  # []
print(get_products_of_all_ints_except_at_index([0]))  # [0]
