#1

def in_asc_order(arr):
    return arr == sorted(arr)


#2

def mxdiflg(a1, a2):
    if not a1 or not a2:
        return -1
    max_a1, min_a1 = max(map(len, a1)), min(map(len, a1))
    max_a2, min_a2 = max(map(len, a2)), min(map(len, a2))
    return max(abs(max_a1 - min_a2), abs(max_a2 - min_a1))


#3

def flatten_and_sort(array):
    return sorted([num for sublist in array for num in sublist])


#4

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


#5

def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz") 
        else:
            result.append(i)
    return result


#6

def row_weights(array):
    team1 = sum(array[i] for i in range(0,len(array),2))
    team2 = sum(array[i] for i in range(1,len(array),2))
    return (team1, team2)

#7

def greet(name): 
    return f"Hello {name.capitalize()}!"

#8

def is_sorted_and_how(arr):
    if arr == sorted(arr):
        return "yes, ascending"
    elif arr == sorted(arr, reverse=True):
        return "yes, descending"
    else:
        return "no"
    

#9

def remove_duplicate_words(s):
    return ' '.join(sorted(set(s.split()), key = s.index))