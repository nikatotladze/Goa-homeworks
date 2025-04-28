# 1

def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))


# 2

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)

# 3

def row_sum_odd_numbers(n):
    return n ** 3

# 4

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

# 5

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))

# 6

def binary_array_to_number(arr):
    return int("".join(map(str, arr)), 2)

# 7

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

# 8

def oddOrEven(arr):
    return "odd" if sum(arr)%2 else "even"

# 9

def min_max(lst):
  return [min(lst), max(lst)]

# 10

def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

# 11

def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

# 12

def number(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

# 13

def divisors(n):
    return  len([l_div for l_div in range(1, n + 1) if n % l_div == 0]);

# 14

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
        
# 15

def breakChocolate(n, m):
    return max(n*m-1,0)
