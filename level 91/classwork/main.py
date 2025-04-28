# 1 

def repeat_str(repeat, string):
    return repeat * string

# 2

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

# 3

def make_negative( number ):
    return -abs(number)

# 4

def positive_sum(arr):
    return sum(x for x in arr if x > 0)

# 5

def row_sum_odd_numbers(n):
    return n ** 3

# 6

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)

# 7

def min_max(lst):
    return [min(lst), max(lst)]

# 8

def divisors(integer):
    result = [i for i in range(2, integer) if integer % i == 0]
    return result if result else f"{integer} is prime"
