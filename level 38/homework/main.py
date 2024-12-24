#1

def area_or_perimeter(l, w):
    # თუ სიგრძე და სიგანე ტოლია
    if l == w:
        return l * w  # დააბრუნე ფართობი
    else:
        return 2 * (l + w)  # დააბრუნე პერიმეტრი


#2

def other_angle(a, b):
    return 180 - (a + b)


#3

def set_alarm(employed, vacation):
    return employed and not vacation


#4

def sum_mix(arr):
    return sum(int(x) for x in arr)

#5

def sum_array(arr):
    if arr is None:
        return 0 
    return sum(arr)
