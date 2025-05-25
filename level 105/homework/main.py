# 1

def cube_odd(arr):
    if any(type(x) is not int for x in arr):
        return None
    return sum(x ** 3 for x in arr if x % 2 != 0)


# 2

def geometric_sequence_sum(a, r, n):
    if r != 1:
        return a * (r ** n - 1) / (r - 1) 
    else:
        return a * n
    

# 3

def seqlist(first, skipBy, count):
    last = (skipBy * count) + first
    return list(range(first, last, skipBy))


# 4

def shift_left(a, b, n=0):
    if a == b:
        return n
    elif len(a)>len(b):
        return shift_left(a[1:], b, n + 1)
    else:
        return shift_left(a, b[1:], n + 1)
    

# 5

def encode(s):
    return ''.join(str(ord(x) - ord('a') + 1) if x.isalpha() else x for x in s.lower())