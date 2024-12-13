#1

#1

def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()


#2

def areYouPlayingBanjo(name):
    if name[0].lower() == 'r':
        return name + ' plays banjo'
    else:
        return name + ' does not play banjo'
    

#3

def simple_multiplication(number) :
    return number * 9 if number % 2 else number * 8

#4


def find_needle(haystack):
    return f'found the needle at position {haystack.index("needle")}'


#5

def invert(lst):
    return [-x for x in lst]