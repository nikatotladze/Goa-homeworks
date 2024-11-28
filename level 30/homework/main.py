#1


# 1

def opposite(number):
    return -number


# 2 

def sum_array(a):
  return sum(a)


# 3

def paperwork(n, m):
    # If either n or m is negative or zero, return 0
    if n <= 0 or m <= 0:
        return 0
    # Otherwise, return the product of n and m
    return n * m



# 4

def past(h, m, s):
    # Convert hours, minutes, and seconds to milliseconds and return the total
    return (h * 3600000) + (m * 60000) + (s * 1000)


# 5

def make_upper_case(strng):
    return strng.upper()


# 2

def manual_replace(string, old, new):
    result = ""
    i = 0
    while i < len(string):
        # თუ old ქვე-სტრიქონი ნაპოვნია
        if string[i:i+len(old)] == old:
            result += new
            i += len(old)  # გადავსწიოთ index ძველ ქვე-სტრიქონის ზომით
        else:
            result += string[i]
            i += 1
    return result

# მაგალითი
print(manual_replace("hello world", "world", "Python"))  # Output: "hello Python"


# 3

def manual_len(string):
    count = 0
    for _ in string:
        count += 1
    return count

# მაგალითი
print(manual_len("hello world"))  # Output: 11
