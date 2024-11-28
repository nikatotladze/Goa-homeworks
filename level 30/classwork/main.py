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
    return [int(d) for d in str(n)][::-1]