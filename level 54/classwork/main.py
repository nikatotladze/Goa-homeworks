#1

# list, dict, set, bytearray.


#2
 
# int, float, str, tuple, frozenset, bytes.


#3

# lambda ფუნქციას მეორენაირად უწოდებენ ანონიმურ ფუნქციას


#4

# map: გამოიყენება თითოეულ ელემენტზე ოპერაციის ჩასატარებლად და შედეგების ახალი კოლექციის შესაქმნელად.

# filter:  გამოიყენება ისეთი ელემენტების ამოსარჩევად, რომლებიც აკმაყოფილებენ კონკრეტულ პირობას.


#5

# ორი სტრინგის შეერთებას ეწოდება კონკატენაცია


#6


numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  


celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)  


words = ["hello", "world", "python"]
capitalized_words = list(map(lambda w: w.capitalize(), words))
print(capitalized_words) 



#7


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 


strings = ["cat", "house", "tree", "car"]
long_strings = list(filter(lambda s: len(s) >= 4, strings))
print(long_strings) 


numbers = [3, 9, 15, 22, 27, 30]
multiples_of_three = list(filter(lambda x: x % 3 == 0, numbers))
print(multiples_of_three) 
