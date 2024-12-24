#1

def get_count(sentence):
    vowels = "aeiou"
    return sum(1 for char in sentence if char in vowels)


#2

def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string_ if char not in vowels)

#3

def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))

