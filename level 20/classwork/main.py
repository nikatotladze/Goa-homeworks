# 1) 5 ელემენტიანი List-ის შექმნა და 2 ელემენტიდან ბოლო ელემენტის ჩათვლით გამოყვანა
list_1 = [10, 20, 30, 40, 50]
print("2 ელემენტიდან ბოლო ელემენტამდე:", list_1[1:])

# 2) 5 ელემენტიანი List-ის შექმნა და თავიდან ბოლოს წინა ელემენტამდე გამოყვანა
list_2 = [5, 15, 25, 35, 45]
print("თავიდან ბოლოს წინა ელემენტამდე:", list_2[:-1])

# 3) String-ის შექმნა და მის შებრუნება slicing-ის მეშვეობით
my_string = "Python"
reversed_string = my_string[::-1]
print("შებრუნებული სტრინგი:", reversed_string)
