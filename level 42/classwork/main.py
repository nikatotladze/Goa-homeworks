<<<<<<< HEAD
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
=======
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
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
    return min(len(word) for word in s.split())