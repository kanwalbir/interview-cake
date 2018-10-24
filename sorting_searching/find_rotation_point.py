# Time: O(logn)
# Space: O(1)


def find_rotation_point(words):

    start = 0
    end = len(words) - 1

    while start < end:
        mid = (end + start) // 2

        if words[mid-1] > words[mid]:
            return mid
        
        if words[mid] > words[mid+1]:
            return mid+1 

        if words[0] < words[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


words = ['paint', 'ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']
print(find_rotation_point(words))  # 6

words = ['asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']
print(find_rotation_point(words))  # -1

words = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'asymptote']
print(find_rotation_point(words))  # 4

words = ['cape', 'cake']
print(find_rotation_point(words))  # 1

words = ['grape', 'orange', 'plum', 'radish', 'apple']
print(find_rotation_point(words))  # 4

words = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage']
print(find_rotation_point(words))  # 5
