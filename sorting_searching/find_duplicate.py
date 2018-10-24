# Time: O(nlogn)
# Space: O(1) - Save the orginal input list


def find_repeat(the_list):
    
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        mid = (ceiling + floor) // 2
        potential_num_in_lower_range = mid - floor + 1
        actual_num_in_lower_range = 0

        for num in the_list:
            if num >= floor and num <= mid:
                actual_num_in_lower_range += 1

        if actual_num_in_lower_range > potential_num_in_lower_range:
            ceiling = mid
        else:
            floor = mid + 1

    return floor


print(find_repeat([2, 1, 0, 1]))  # 1
print(find_repeat([1, 1]))  # 1
print(find_repeat([1, 2, 3, 2]))  # 2
print(find_repeat([1, 2, 5, 5, 5, 5]))  # 5
print(find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5]))  # 4
print(find_repeat([4, 4, 4, 4, 3, 2, 7, 6, 5]))  # 4
