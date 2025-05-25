# 1


def capitalize(s, ind):
    result = list(s) 
    for i in ind:
        if 0 <= i < len(result):  
            result[i] = result[i].upper()  
    return ''.join(result)  


