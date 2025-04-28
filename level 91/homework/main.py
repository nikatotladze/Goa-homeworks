#1

def smash(words):
    return " ".join(words)

# 2

def grow(arr):
	product = 1
	for i in arr:
		product *= i
	return product

# 3

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# 4

def better_than_average(class_points, your_points):
    return your_points > sum(class_points) / len(class_points)

# 5

def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result


# 6

def string_to_array(string):
    return string.split(" ")


# 7

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

# 8

def reverseseq(n):
    return list(range(n, 0, -1))


# 9

def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"


# 10

def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)

# 11

def check_for_factor(base, factor):
    return base % factor == 0

# 12

def hoopCount(n):
    return "Keep at it until you get it" if n<10 else "Great, now move on to tricks"


# 13

def get_average(marks):
    return sum(marks) // len(marks)


# 14

def reverseWords(str):
    return " ".join(str.split(" ")[::-1])


# 15

def make_negative( number ):
    return -abs(number)


# 16

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


# 17

def repeat_str(repeat, string):
    return string*repeat


# 18

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2


# 19

def make_upper_case(s): return s.upper()

# 20

def find_average(array):
    return sum(array) / len(array) if array else 0
