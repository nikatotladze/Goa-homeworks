# 1

def spin_words(sentence):
    return ' '.join(
        word[::-1] if len(word) >= 5 else word
        for word in sentence.split()
    )


# 2

def encode(st):
    vowel_to_num = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
    return ''.join(vowel_to_num.get(char, char) for char in st)

def decode(st):
    num_to_vowel = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    return ''.join(num_to_vowel.get(char, char) for char in st) 