#1

def count_red_beads(n):
    return(n-1)*2


#2

def generateShape(integer):
    return '\n'.join('+' * integer for i in range(integer))


#3

def bumps(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"


#4

def adjacent_element_product(array):
    return max(array[i]*array[i+1] for i in range(len(array)-1))


#5

def filter_string(string):
    return int(''.join(filter(str.isdigit, string)))