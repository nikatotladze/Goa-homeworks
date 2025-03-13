# 1

def count_repeats(txt):
    result = 0
    repeats = ""
    for i in txt:
        if i != repeats:
            repeats = i
        elif i == repeats:
            result+=1
    return result


# 2

def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

# 3

def sortme(words):
    return sorted(words, key=str.lower)