# Time: O(n)
# Space: O(1)

import random


def shuffle(the_list):

    for i in range(len(the_list)-1):
        r = random.randint(i, len(the_list)-1)
        if i != r:
            the_list[i], the_list[r] = the_list[r], the_list[i]

    return (the_list)


print(shuffle([20, 15, 30, 40, 5, 0]))
print(shuffle([1, 2, 3, 4, 5]))
print(shuffle([100]))
print(shuffle([]))
