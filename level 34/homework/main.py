<<<<<<< HEAD
#1

#1

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


#2

def string_to_array(string):
    return string.split(" ")


#3

def check(seq, elem):
    return elem in seq

#4

def reverseseq(n):
    return list(range(n, 0, -1))

#5

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]



#2

def manual_min(numbers):
    if not numbers:  # თუ სია ცარიელია
        return None
    minimum = numbers[0]  # პირველი ელემენტი როგორც საწყისი მინიმუმი
    for num in numbers:  # გავიაროთ სია
        if num < minimum:  # ვნახოთ თუ ელემენტი ნაკლებია მინიმუმზე
            minimum = num
    return minimum


#3

def manual_max(numbers):
    if not numbers:  # თუ სია ცარიელია
        return None
    maximum = numbers[0]  # პირველი ელემენტი როგორც საწყისი მაქსიმუმი
    for num in numbers:  # გავიაროთ სია
        if num > maximum:  # ვნახოთ თუ ელემენტი მეტია მაქსიმუმზე
            maximum = num
    return maximum
=======
#1

#1

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)


#2

def string_to_array(string):
    return string.split(" ")


#3

def check(seq, elem):
    return elem in seq

#4

def reverseseq(n):
    return list(range(n, 0, -1))

#5

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]



#2

def manual_min(numbers):
    if not numbers:  # თუ სია ცარიელია
        return None
    minimum = numbers[0]  # პირველი ელემენტი როგორც საწყისი მინიმუმი
    for num in numbers:  # გავიაროთ სია
        if num < minimum:  # ვნახოთ თუ ელემენტი ნაკლებია მინიმუმზე
            minimum = num
    return minimum


#3

def manual_max(numbers):
    if not numbers:  # თუ სია ცარიელია
        return None
    maximum = numbers[0]  # პირველი ელემენტი როგორც საწყისი მაქსიმუმი
    for num in numbers:  # გავიაროთ სია
        if num > maximum:  # ვნახოთ თუ ელემენტი მეტია მაქსიმუმზე
            maximum = num
    return maximum
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
