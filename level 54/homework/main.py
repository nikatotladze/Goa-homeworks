#2

numbers = [2, 4, 6, 8, 10]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  


#3

names = ["Alice", "Bob", "Charlie"]
greetings = list(map(lambda name: "Hello, " + name, names))
print(greetings)  


#4

words = ["apple", "banana", "kiwi"]
lengths = list(map(len, words))
print(lengths)  


#5

numbers = [-5, 3, -2, 7, 0, 10]
positives = list(filter(lambda x: x > 0, numbers))
print(positives)  


#6

words = ["pear", "apple", "peach", "grape"]
p_words = list(filter(lambda word: word.startswith('p'), words))
print(p_words)  


#7

numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)  

