# Time: O(n)
# Space: O(n)


def split_words(input_string):

    start = length = 0
    words = []

    for idx, char in enumerate(input_string + '.'):
        if char.isalpha():
            length += 1
        elif char in ('-', "'") and length:
            length += 1
        else:
            if length:
                curr_word = input_string[start:start+length]
                words.append(curr_word)
                length = 0
            start = idx + 1
    
    return words


def create_word_cloud(input_string):

    words = split_words(input_string)
    words_to_counts = {}
    
    for word in words:
        if word in words_to_counts:
            words_to_counts[word] += 1            
        elif word.lower() in words_to_counts:
            words_to_counts[word.lower()] += 1
        elif word.upper() in words_to_counts:
            words_to_counts[word.upper()] += 1
        elif word.capitalize() in words_to_counts:
            words_to_counts[word] = words_to_counts[word.capitalize()] + 1
            del words_to_counts[word.capitalize()]
        else:
            words_to_counts[word] = 1

    return words_to_counts


input1 = 'After beating the eggs, Dana read the next step:'
print(create_word_cloud(input1))
print()
input2 = 'Add milk and eggs, then add flour and sugar.'
print(create_word_cloud(input2))
print()
input3 = 'Add milk and eggs, then add flour and sugar'
print(create_word_cloud(input3))
print()
input4 = 'After beating the eggs, Dana read the next-step:'
print(create_word_cloud(input4))
print()
input5 = 'After beating the eggs, Dana read the next - step:'
print(create_word_cloud(input5))
print()
input6 = "We came, we saw, we conquered...then we ate Bill's (Mille-Feuille) cake."
print(create_word_cloud(input6))
print()
input7 = 'The bill came to five dollars.'
print(create_word_cloud(input7))
print()
input8 = 'Mmm...mmm...Decisions...decisions'
print(create_word_cloud(input8))
print()
input9 = "Allie's Bakery: Sasha's Cakes"
print(create_word_cloud(input9))
print()
print(create_word_cloud(''))
print()
print(create_word_cloud(' '))
print()
print(create_word_cloud('.;!'))
