#1

#1

def find_average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)  # Calculate the average



#2

def smash(words):
    return " ".join(words)


#3

from functools import reduce

def grow(arr):
    return reduce(lambda x, y: x * y, arr)


#4

def hero(bullets, dragons):
    return bullets >= dragons * 2


# 5

def better_than_average(class_points, your_points):
    return your_points > (sum(class_points) / len(class_points))


#2

def manual_find(text, substring):
    for i in range(len(text) - len(substring) + 1):
        if text[i:i + len(substring)] == substring:
            return i
    return -1

# მაგალითი გამოყენება:
print(manual_find("hello world", "world"))  # აჩვენებს 6
print(manual_find("hello world", "Python"))  # აჩვენებს -1



#3

def manual_swapcase(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':  # თუ პატარა ასოა
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':  # თუ დიდი ასოა
            result += chr(ord(char) + 32)
        else:  # სხვა სიმბოლოები უცვლელი რჩება
            result += char
    return result

# მაგალითი გამოყენება:
print(manual_swapcase("Hello World"))  # აჩვენებს "hELLO wORLD"
print(manual_swapcase("Python3.8"))   # აჩვენებს "pYTHON3.8"
