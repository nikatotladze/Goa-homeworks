#1

def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1 , integer)]


#2

name = "codewa.rs"


#3

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res += [i]
        i += 1
    return res


#4

def xor(a,b):
    return a != b


#5

def get_real_floor(n):
    if n <= 0:
        return n
    elif n >= 13:
        return n - 2
    else:
        return n - 1
    

#6

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    return [bird for bird in birds if bird not in geese]

#7

def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

#8

def name_shuffler(str_):
    return ' '.join(str_.split(' ')[::-1])


#9

def pipe_fix(nums):
    return list(range(min(nums), max(nums) + 1))


#10

def sale_hotdogs( _n ):
    if _n < 5:
        return _n * 100
    elif _n >= 10:
        return _n * 90
    else:
        return _n * 95