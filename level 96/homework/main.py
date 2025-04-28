# 1

def main(verb, noun): 
    return verb + noun


# 2

def nth_even(n):
    return 2 * (n - 1);


# 3

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)


# 4

def unusual_five():
    return len("five!")


# 5

def add_length(str_):
    return ["{} {}".format(i, len(i)) for i in str_.split(' ')]


# 6

def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'
        


# 7

def flip(d,a):
    return sorted(a, reverse=d=='L')

# 8

def well(x):
    if x.count("good") == 0:
        return "Fail!"
    elif x.count("good") <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
    

# 9

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# 10

def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')


# 11

def to_binary(n):
    return int(f'{n:b}')


# 12

def to_binary(n):
    return int(f'{n:b}')


# 13

def square_or_square_root(arr):
    result = []
    for x in arr:
        root = x**0.5
        if root.is_integer():
            result.append(root)
        else:
            result.append(x*x)
    return result


# 14

def no_boring_zeros(n):
    try:
        return int(str(n).rstrip('0'))
    except ValueError:
        return 0
    

# 15

def _if(bool, func1, func2):
  if bool:
      func1()
  else:
      func2()