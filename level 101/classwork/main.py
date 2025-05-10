# 1

def solve(a, b):
    result = ''
    for c in a:
        if c not in b:
            result += c
    for c in b:
        if c not in a:
            result += c
    return result


# 2

def largest_sum(a):
    substrings = a.split('0')
    max_sum = 0
    for s in substrings:
        current = sum(int(digit) for digit in s)
        if current > max_sum:
            max_sum = current
    return max_sum