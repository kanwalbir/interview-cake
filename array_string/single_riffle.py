# Time: O(n)
# Space: O(1)


def is_single_riffle(half1, half2, shuffled_deck):

    i = j = 0
    for card in shuffled_deck:
        if (i < len(half1)) and (half1[i] == card):
            i += 1
        elif (j < len(half2)) and (half2[j] == card):
            j += 1
        else:
            return False
    return True


print(is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))  # True
print(is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5]))  # False
print(is_single_riffle([], [], []))  # True
print(is_single_riffle([], [2, 3, 6], [2, 3, 6]))  # True
print(is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5]))  # False
print(is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]))  # False
