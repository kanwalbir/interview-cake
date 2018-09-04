# Time: O(n)
# Space: O(1)


def reverse_strings(message, li, ri):
    while (li < ri):
        message[li], message[ri] = message[ri], message[li]
        li += 1
        ri -= 1


def reverse_words(message):
    
    reverse_strings(message, 0, len(message) - 1)
    li = 0
    for ri in range(len(message)+1):
        if ri == len(message) or message[ri] == ' ':
            reverse_strings(message, li, ri-1)
            li = ri + 1


message1 = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
print(message1)
reverse_words(message1)
print(message1)
print()

message2 = [ 'c', 'a', 'k', 'e']
print(message2)
reverse_words(message2)
print(message2)
print()

message3 = [ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd']
print(message3)
reverse_words(message3)
print(message3)
print()

message4 = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l', ' ',
            'y', 'u', 'm']
print(message4)
reverse_words(message4)
print(message4)
print()

message5 = []
print(message5)
reverse_words(message5)
print(message5)
print()

message6 = [' ']
print(message6)
reverse_words(message6)
print(message6)
print()

message7 = list('rat the ate cat the')
print(message7)
reverse_words(message7)
print(message7)
print()

message8 = list('yummy is cake bundt chocolate')
print(message8)
reverse_words(message8)
print(message8)
expected = list('chocolate bundt cake is yummy')
