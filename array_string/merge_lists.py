# Time: O(n)
# Space: O(n)

import heapq


def merge_lists(list1, list2):
    i = j = 0
    combined = []

    while (i < len(list1)) or (j < len(list2)):

        if i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                combined.append(list1[i])
                i += 1
            else:
                combined.append(list2[j])
                j += 1
        elif i < len(list1):
            combined.append(list1[i])
            i += 1
        elif j < len(list2):
            combined.append(list2[j])
            j += 1
    
    # combined_heap = list(heapq.merge(list1, list2))
    # print(combined_heap)

    return combined


list1 = [3, 4, 6, 10, 11, 15]
list2 = [1, 5, 8, 12, 14, 19, 20]
print(merge_lists(list1, list2))

list1 = [3, 4, 6, 10, 11, 15]
list2 = []
print(merge_lists(list1, list2))

list1 = []
list2 = []
print(merge_lists(list1, list2))
