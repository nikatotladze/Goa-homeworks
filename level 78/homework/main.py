# 1

def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return "%s likes this" % names[0]
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    else:
        return "%s, %s and %s others like this" % (names[0], names[1], len(names)-2)
    


# 2

def dig_pow(n, p):
    sum = 0
    for c in str(n):
        sum += int(c) ** p
        p += 1
    if sum % n == 0:
        return sum / n
    else:
        return -1
    


# 3

def matrix_div(r,m,n):
    if n == 0:
        return [[r[j][i][i] / m[i][i] for i in range(len(m))] for j in range(len(m))]
    else:
        return [[r[i][j][i] / m[i][i] for j in range(len(m))] for i in range(len(m))]
    

# 4

def draw_stairs(n):
    return '\n'.join(' '*i+'I' for i in range(n))


# 5

def usdcny(usd):
    return f"{(usd * 6.75):.2f} Chinese Yuan"