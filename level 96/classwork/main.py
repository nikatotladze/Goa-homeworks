# 1

def bin_to_decimal(inp):
    return int(inp, 2)


# 2

def replace_dots(string):
    return string.replace('.', '-')

# 3

def mango(quantity, price):
    return (quantity - quantity // 3) * price

# 4

def get_size(w, h, d):
    area = 2*(w*h + h*d + w*d)
    volume = w*h*d
    return [area, volume]

# 5

def duty_free(price, discount, holiday_cost):
  return holiday_cost // (price * (discount / 100))


# 6

def remove(s):
    return s[:-1] if s.endswith('!') else s


# 7

def hex_to_dec(s):
    return int(s, 16)


# 8

def say_hello(name, city, state):
  return "Hello, {}! Welcome to {}, {}!".format(" ".join(name), city, state)


# 9

def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet) - 96)


# 10

def take(arr,n):
    return arr[:n]


# 11

def reverse(st):
    return " ".join(st.split()[::-1])


# 12

def find_average(nums):
    return sum(nums) / len(nums) if nums else 0


# 13

def whatday(num):
  switcher = {
      1:'Sunday',
      2:'Monday',
      3:'Tuesday',
      4:'Wednesday',
      5:'Thursday',
      6:'Friday',
      7:'Saturday'
  }
  return switcher.get(num, 'Wrong, please enter a number between 1 and 7')


# 14

def print_array(arr):
    return ','.join(map(str, arr))


# 15

def remainder(a,b):
    if min(a,b) == 0:
        return None
    elif a > b:
        return a % b
    else: 
        return b % a