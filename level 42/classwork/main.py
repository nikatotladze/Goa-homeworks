#1 ?


#2

def xo(s):
    s = s.lower()  
    return s.count('x') == s.count('o')


#3

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())


#5

def find_short(s):
    return min(len(word) for word in s.split())