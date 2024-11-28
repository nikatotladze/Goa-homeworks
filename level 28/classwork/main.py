# 1

def remove_char(s):
    return s[1: -1]

# 2

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)


# 3

def find_smallest_int(arr):
    return min(arr)


# 4

def string_to_number(s):
    # ... your code here
    try:
        return int(s)
    except (ValueError):
        return "Input is not valid " 
    

# 5

def summation(num):
    return sum(range(1,num+1))
    

# 6

def greet():
    return "hello world!"