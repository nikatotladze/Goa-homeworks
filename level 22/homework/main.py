<<<<<<< HEAD
# 2 შექმენით ფუნქცია რომელიც დააბრუნებს "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount"

def check_discount(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didn't get discount"

# ტესტირება
print(check_discount(15))  # დააბრუნებს "You got discount"
print(check_discount(20))  # დააბრუნებს "You didn't get discount"


# 3 შექმენით ფუნქცია manual_reverse, რომელიც არგუმენტად მიიღებს string'ს და დააბრუნებს ამ string'ს ოღონდ შეტრიალებულად

def manual_reverse(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# ტესტირება
print(manual_reverse("Hello"))  # დააბრუნებს "olleH"


# 4 გატესტეთ .upper(), .lower(), .capitalize(), .swapcase() და .find() მეთოდები

text = "Hello World"

# .upper() - ყველა ასოს დიდ ასოებად გადაქცევა
print(text.upper())  # "HELLO WORLD"

# .lower() - ყველა ასოს მცირე ასოებად გადაქცევა
print(text.lower())  # "hello world"

# .capitalize() - პირველი ასოს დიდ ასოდ გადაქცევა
print(text.capitalize())  # "Hello world"

# .swapcase() - ყველა ასოს საწინააღმდეგო რეგისტრში გადაყვანა
print(text.swapcase())  # "hELLO wORLD"

# .find() - პირველი წინასწარ განსაზღვრული სიმბოლოს ან ქვე-სტრინგის ინდექსის პოვნა
print(text.find("World"))  # 6 (დაბრუნდება "World"-ის პირველი ასოს ინდექსი)


# 5 ახსენით რატომ ჰქვიათ ამ ფუნქციებს მეთოდები

# ამ ფუნქციებს ჰქვიათ მეთოდები, რადგან ისინი დაკავშირებულია კონკრეტულ მონაცემთა ტიპზე 

# 6 ახსენით რა არის dot notation და რა შემთხვევაში გამოიყენება

=======
# 2 შექმენით ფუნქცია რომელიც დააბრუნებს "You got discount" თუ მომხმარებელი არის არასრულწლოვანი, სხვა შემთხვევაში დააბრუნებს "You didn't get discount"

def check_discount(age):
    if age < 18:
        return "You got discount"
    else:
        return "You didn't get discount"

# ტესტირება
print(check_discount(15))  # დააბრუნებს "You got discount"
print(check_discount(20))  # დააბრუნებს "You didn't get discount"


# 3 შექმენით ფუნქცია manual_reverse, რომელიც არგუმენტად მიიღებს string'ს და დააბრუნებს ამ string'ს ოღონდ შეტრიალებულად

def manual_reverse(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# ტესტირება
print(manual_reverse("Hello"))  # დააბრუნებს "olleH"


# 4 გატესტეთ .upper(), .lower(), .capitalize(), .swapcase() და .find() მეთოდები

text = "Hello World"

# .upper() - ყველა ასოს დიდ ასოებად გადაქცევა
print(text.upper())  # "HELLO WORLD"

# .lower() - ყველა ასოს მცირე ასოებად გადაქცევა
print(text.lower())  # "hello world"

# .capitalize() - პირველი ასოს დიდ ასოდ გადაქცევა
print(text.capitalize())  # "Hello world"

# .swapcase() - ყველა ასოს საწინააღმდეგო რეგისტრში გადაყვანა
print(text.swapcase())  # "hELLO wORLD"

# .find() - პირველი წინასწარ განსაზღვრული სიმბოლოს ან ქვე-სტრინგის ინდექსის პოვნა
print(text.find("World"))  # 6 (დაბრუნდება "World"-ის პირველი ასოს ინდექსი)


# 5 ახსენით რატომ ჰქვიათ ამ ფუნქციებს მეთოდები

# ამ ფუნქციებს ჰქვიათ მეთოდები, რადგან ისინი დაკავშირებულია კონკრეტულ მონაცემთა ტიპზე 

# 6 ახსენით რა არის dot notation და რა შემთხვევაში გამოიყენება

>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
#Dot notation არის სინტაქსი, რომელიც გამოიყენება ობიექტზე მეთოდების ან თვისებების წვდომისთვის. 