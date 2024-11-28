#3

my_list = [10, 20, 30, 40, 50, 60, 70]
removed_element = my_list.pop(5)  # შლის მეექვსე ელემენტს (ინდექსი 5)
print(removed_element)  # შედეგი: 60
print(my_list)  # შედეგი: [10, 20, 30, 40, 50, 70]


#4

my_list = [1, 2, 3, 4, 5]
my_list.remove(2)  # შლის მნიშვნელობით მეორე ელემენტს
print(my_list)  # შედეგი: [1, 3, 4, 5]


#5

my_list = [1, 2, 3, 4]
my_list.append(5)  # ამატებს 5-ს ბოლოში
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]


#6

my_list = [1, 3, 4, 5]
my_list.insert(1, 2)  # ჩაამატებს 2-ს მეორე ელემენტად (ინდექსი 1)
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]


#7

my_list = [1, 2, 3, 4, 5]
my_list.pop()  # შლის ბოლო ელემენტს
print(my_list)  # შედეგი: [1, 2, 3, 4]


#8

my_list = [1, 2, 3, 4, 5]
count = len(my_list)  # ითვლის ელემენტების რაოდენობას
print(count)  # შედეგი: 5


#9

my_string = "Hello, world!"
char_count = len(my_string)  # ითვლის სიმბოლოების რაოდენობას
print(char_count)  # შედეგი: 13
