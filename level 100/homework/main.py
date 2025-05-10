# 1 

def validate_base(num, base):
    valid_digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base]
    return all(char in valid_digits for char in num)


# 2

def comes_after(st, l): 
    result = ''
    l = l.lower()
    for i in range(len(st) - 1):
        if st[i].lower() == l and st[i + 1].isalpha():
            result += st[i + 1]
    return result


# 3

import math

def stack_height_2d(layers):
    if layers == 0:
        return 0
    return 1 + (layers - 1) * (math.sqrt(3) / 2)


# 4

def change(st):
    result = ['0'] * 26
    for char in st.lower():
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            result[index] = '1'
    return ''.join(result)



# 5

def chain(init_val, functions):
    for func in functions:
        init_val = func(init_val)
    return init_val


# 6

def largest_sum(a):
    substrings = a.split('0')
    max_sum = 0
    for s in substrings:
        current = sum(int(digit) for digit in s)
        if current > max_sum:
            max_sum = current
    return max_sum



# 7


def bits_battle(numbers):
    odd_ones = 0
    even_zeros = 0
    
    for n in numbers:
        if n == 0:
            continue
        binary = bin(n)[2:]
        if n % 2 == 1:
            odd_ones += binary.count('1')
        else:
            even_zeros += binary.count('0')
    
    if odd_ones > even_zeros:
        return 'odds win'
    elif even_zeros > odd_ones:
        return 'evens win'
    else:
        return 'tie'


# 8

def decode(message):
    return ''.join(chr(219 - ord(c)) if c.isalpha() else c for c in message)

# 9

def invert_hash(dictionary):
    return {v: k for k, v in dictionary.items()}

# 10

def create_box(m, n):
    box = [[0] * m for _ in range(n)]
    layers = min(m, n) // 2 + (min(m, n) % 2 != 0)
    
    for layer in range(layers):
        value = layer + 1
        for i in range(layer, n - layer):
            for j in range(layer, m - layer):
                box[i][j] = value
    return box
