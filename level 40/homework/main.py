<<<<<<< HEAD
#1

def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return f"{max(numbers)} {min(numbers)}"


#2

def filter_list(l):
    return [x for x in l if isinstance(x, int)]


#3

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


#4

import math

def is_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n


#5

def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]
=======
#1

def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))
    return f"{max(numbers)} {min(numbers)}"


#2

def filter_list(l):
    return [x for x in l if isinstance(x, int)]


#3

def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


#4

import math

def is_square(n):
    return n >= 0 and math.isqrt(n) ** 2 == n


#5

def get_middle(s):
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return s[mid - 1:mid + 1]
    else:
        return s[mid]
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
