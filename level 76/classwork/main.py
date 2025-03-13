# 1

def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


# 2

def diamond(n):
        return (n>0 and n%2==1)*"".join(str.rstrip(str.center("*"*(n-2*abs(n//2-x)),n))+"\n" for x in range(n)) or None