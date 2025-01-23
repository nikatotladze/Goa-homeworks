<<<<<<< HEAD
# 2) Lambda ფუნქცია, რომელიც აბრუნებს 2 სტრინგის ჯამს
concat_strings = lambda s1, s2: s1 + s2

# 3) Lambda ფუნქცია, რომელიც აბრუნებს 3 რიცხვის ჯამს
sum_three_numbers = lambda a, b, c: a + b + c

# 4) Lambda ფუნქცია, რომელიც იღებს list-ს და აბრუნებს მასში მყოფი რიცხვების ჯამს
sum_list = lambda lst: sum(lst)

# 5) Lambda ფუნქცია, რომელიც იღებს string-ს და რაიმე სიმბოლოს და აბრუნებს, რამდენჯერ მეორდება სიმბოლო string-ში
count_symbol = lambda string, symbol: string.count(symbol)

# გამოყენების მაგალითები:
print(concat_strings("Hello, ", "World!"))  # "Hello, World!"
print(sum_three_numbers(1, 2, 3))           # 6
print(sum_list([1, 2, 3, 4]))               # 10
print(count_symbol("banana", "a"))          # 3

# 6


#1

def make_negative( number ):
    return -abs(number)


#2

def bool_to_word(bool):
    return "Yes" if bool else "No"


#3

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


#4

def repeat_str(repeat, string):
    return repeat * string


#5

def lovefunc( flower1, flower2 ):
=======
# 2) Lambda ფუნქცია, რომელიც აბრუნებს 2 სტრინგის ჯამს
concat_strings = lambda s1, s2: s1 + s2

# 3) Lambda ფუნქცია, რომელიც აბრუნებს 3 რიცხვის ჯამს
sum_three_numbers = lambda a, b, c: a + b + c

# 4) Lambda ფუნქცია, რომელიც იღებს list-ს და აბრუნებს მასში მყოფი რიცხვების ჯამს
sum_list = lambda lst: sum(lst)

# 5) Lambda ფუნქცია, რომელიც იღებს string-ს და რაიმე სიმბოლოს და აბრუნებს, რამდენჯერ მეორდება სიმბოლო string-ში
count_symbol = lambda string, symbol: string.count(symbol)

# გამოყენების მაგალითები:
print(concat_strings("Hello, ", "World!"))  # "Hello, World!"
print(sum_three_numbers(1, 2, 3))           # 6
print(sum_list([1, 2, 3, 4]))               # 10
print(count_symbol("banana", "a"))          # 3

# 6


#1

def make_negative( number ):
    return -abs(number)


#2

def bool_to_word(bool):
    return "Yes" if bool else "No"


#3

def positive_sum(arr):
    return sum(x for x in arr if x > 0)


#4

def repeat_str(repeat, string):
    return repeat * string


#5

def lovefunc( flower1, flower2 ):
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
    return (flower1+flower2)%2