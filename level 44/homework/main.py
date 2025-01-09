#1

def longest(a1, a2):
    return ''.join(sorted(set(a1 + a2)))


#2

def open_or_senior(data):
    return ["Senior" if age >= 55 and handicap > 7 else "Open" for age, handicap in data]


#3

import math

def find_next_square(sq):
    # Check if the number is a perfect square
    if math.isqrt(sq) ** 2 == sq:
        # Find the next perfect square
        next_square = (math.isqrt(sq) + 1) ** 2
        return next_square
    else:
        return -1


#4

