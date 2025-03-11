#1

def find_children(dancing_brigade):
    return ''.join(sorted(dancing_brigade, key=lambda x: (x.upper(), x.islower())))

#2

def string_transformer(s):
    return ' '.join(word.swapcase() for word in s.split(' ')[::-1])


#3

def hamming(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count
