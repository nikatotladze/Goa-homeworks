#1

def create_phone_number(n):
    return f"({n[0]}{n[1]}{n[2]}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"


#2

def likes(names):
    if not names:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"



#3

def find_it(seq):
    for num in seq:
        if seq.count(num) % 2 != 0:
            return num
        

#4

def move_zeros(lst):
    non_zero = [x for x in lst if x != 0]
    zero = [0] * (len(lst) - len(non_zero))
    return non_zero + zero