#1

numbers = [25, 40, 15, 50, 60, 30, 90, 10]
filtered_numbers = list(filter(lambda x: x >= 40, numbers))
print(filtered_numbers)  


#2

numbers = [2, 4, 6, 8, 10]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  


#3

strings = ["apple", "banana", "grape", "avocado", "mango", "kiwi"]
filtered_strings = list(filter(lambda s: s.endswith('a'), strings))
print(filtered_strings)  