#1

def final_grade(exam, projects):

    if (exam > 90 or projects > 10):
        results = 100
    elif (exam > 75 and projects >= 5):
        results = 90
    elif (exam > 50 and projects >= 2):
        results = 75
    else:
        results = 0
        
    return results


#2

def expression_matter(a, b, c):
    if 1 not in [a, b, c]:
        return a * b * c
    elif a == 1 and c == 1:
        return a + b + c
    elif a == 1 or (b == 1 and a < c):
        return (a + b) * c
    else:
        return a * (b + c)
    


#3

def sum_str(a, b):
    return str(int('0' + a) + int('0' + b))


#4

def how_much_i_love_you(nb_petals):
    n = nb_petals % 6
    if n == 1:
        return "I love you"
    if n == 2:
        return "a little"
    if n == 3:
        return "a lot"
    if n == 4:
        return "passionately"
    if n == 5:
        return "madly"
    if n == 0:
        return "not at all"
    


#5

def reverse_list(l):
  l.reverse()
  return l


#6

def find_difference(a, b):
	return abs(a[0] * a[1] * a[2] - b[0] * b[1] * b[2])