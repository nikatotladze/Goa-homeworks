#1

def plural(n):
    return n != 1

#2

def problem(a):
    try:
        return a * 50 + 6
    except TypeError:
        return "Error"
    

#3

def multi_table(number):
    return '\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11))


#4

def capitalizeWord(word):
    return word.capitalize()


#5

def add_five(num):
    return num + 5