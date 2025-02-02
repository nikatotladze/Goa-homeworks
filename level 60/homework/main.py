#1

def to_alternating_case(string):
    return string.swapcase()


#2

def correct(string):
    return string.translate(str.maketrans("501", "SOI"))

#3

def bonus_time(salary, bonus):
    return "${}".format(salary * (10 if bonus else 1))

#4

def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

#5

def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

#6

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))