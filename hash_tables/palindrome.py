# Time: O(n)
# Space: O(n) or O(k) or O(1)


def is_palindrome(input_str):

    odd_chars = set()

    for char in input_str:
        if char in odd_chars:
            odd_chars.remove(char)
        else:
            odd_chars.add(char)

    return len(odd_chars) <= 1


print(is_palindrome('sunny'))  # False
print(is_palindrome('civic'))  # True
print(is_palindrome('ivicc'))  # True
print(is_palindrome(''))  # True
