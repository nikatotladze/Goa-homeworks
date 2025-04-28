# 1

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())


# 2

def get_sum(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


# 3

def positive_sum(arr):
    return sum(x for x in arr if x > 0)
