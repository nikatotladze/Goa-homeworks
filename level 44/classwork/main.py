<<<<<<< HEAD
#1

def friend(x):
    return [f for f in x if len(f) == 4]


#2

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]


#3

def add_binary(a,b):
    return bin(a+b)[2:]


#4

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


#5

def is_triangle(a, b, c):
=======
#1

def friend(x):
    return [f for f in x if len(f) == 4]


#2

def maskify(cc):
    return "#"*(len(cc)-4) + cc[-4:]


#3

def add_binary(a,b):
    return bin(a+b)[2:]


#4

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()


#5

def is_triangle(a, b, c):
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
    return (a<b+c) and (b<a+c) and (c<a+b)