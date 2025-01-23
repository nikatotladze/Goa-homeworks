<<<<<<< HEAD
#1

my_list = [1, 2, 3, 4]
print(len(my_list))  # შედეგი: 4


my_list.append(5)
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]


my_list.insert(2, 'a')
print(my_list)  # შედეგი: [1, 2, 'a', 3, 4, 5]


removed_element = my_list.pop(2)
print(removed_element)  # შედეგი: 'a'
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]


my_list.remove(2)
print(my_list)  # შედეგი: [1, 3, 4, 5]


#2

my_list.remove(2)
print(my_list)  # შედეგი: [1, 3, 4, 5]


#3

#.pop() – შლის და აბრუნებს ელემენტს ინდექსის მიხედვით. თუ ინდექსი არ არის მითითებული, ის შლის ბოლო ელემენტს.
#.remove() – შლის სიიდან პირველ ელემენტს, რომელიც მითითებულ მნიშვნელობას ემთხვევა და არ აბრუნებს შედეგს.


#4

my_list = [1, 2, 4, 5]
my_list.insert(2, 3)
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]
=======
#1

my_list = [1, 2, 3, 4]
print(len(my_list))  # შედეგი: 4


my_list.append(5)
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]


my_list.insert(2, 'a')
print(my_list)  # შედეგი: [1, 2, 'a', 3, 4, 5]


removed_element = my_list.pop(2)
print(removed_element)  # შედეგი: 'a'
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]


my_list.remove(2)
print(my_list)  # შედეგი: [1, 3, 4, 5]


#2

my_list.remove(2)
print(my_list)  # შედეგი: [1, 3, 4, 5]


#3

#.pop() – შლის და აბრუნებს ელემენტს ინდექსის მიხედვით. თუ ინდექსი არ არის მითითებული, ის შლის ბოლო ელემენტს.
#.remove() – შლის სიიდან პირველ ელემენტს, რომელიც მითითებულ მნიშვნელობას ემთხვევა და არ აბრუნებს შედეგს.


#4

my_list = [1, 2, 4, 5]
my_list.insert(2, 3)
print(my_list)  # შედეგი: [1, 2, 3, 4, 5]
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
