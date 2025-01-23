<<<<<<< HEAD
# 1

# 1

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator  == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    

# 2 

def litres(time):
    return int(time * 0.5)


# 3

def century(year):
    return (year + 99) // 100


# 4

def maps(a):
    return [x * 2 for x in a]

# 5

def digitize(n):
=======
# 1

# 1

def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator  == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    

# 2 

def litres(time):
    return int(time * 0.5)


# 3

def century(year):
    return (year + 99) // 100


# 4

def maps(a):
    return [x * 2 for x in a]

# 5

def digitize(n):
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
    return [int(d) for d in str(n)][::-1]