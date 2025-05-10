# 1

def move_zeros(lst):
    non_zero = [x for x in lst if x != 0]
    zero = [0] * (len(lst) - len(non_zero))
    return non_zero + zero

# 2

def generate_hashtag(s):
    if not s or s.strip() == "":
        return False

    words = s.strip().split()
    hashtag = '#' + ''.join(word.capitalize() for word in words)

    return hashtag if len(hashtag) <= 140 else False

# 3

def pig_it(text):
    res = []
    
    for i in text.split():
        if i.isalpha():
            res.append(i[1:]+i[0]+'ay')
        else:
            res.append(i)
            
    return ' '.join(res)

# 4

def rot13(message):
    res=''
    for letter in message:
        if letter.isupper():
            res+=chr(65+((ord(letter)-65+13)%26))
        elif letter.islower():
            res+=chr(97+((ord(letter)-97+13)%26))
        else:
            res+=letter
    return res


# 5

opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan


# 6

def domain_name(url):
    if 'www.' in url:
        x = url.split('www.')
        url = x[1]
    if '://' in url:
        x = url.split('://')
        url = x[1]
    if '.' in url:
        x = url.split('.')
        x = x[0]
    return x