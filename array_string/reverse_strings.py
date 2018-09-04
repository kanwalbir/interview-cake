# Time: O(n)
# Space: O(1)


def reverse(list_of_chars):

    if len(list_of_chars) > 1:
        for k in range(len(list_of_chars)//2):
            list_of_chars[k], list_of_chars[-1*k-1] = list_of_chars[-1*k-1], list_of_chars[k]
    return list_of_chars


input1 = ['a','b','c','d','e','f']
print(reverse(input1))
input2 = ['a','b','c','d','e','f','g']
print(reverse(input2))
input3 = ['a']
print(reverse(input3))
input4 = []
print(reverse(input4))
