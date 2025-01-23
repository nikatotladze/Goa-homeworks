<<<<<<< HEAD
#1) შექმენით for loop'ი რომელიც 0'დან 200'მდე დაპრინტავს ყოველ მეექვსე რიცხვს

for i in range(0, 201, 6):
    print(i)


#2) გადაატეთ for loop'ი სტრინგს: "Goodbye World!"

string = "Goodbye World!"
for char in string:
    print(char)


#3) შექმენით for loop'ი რომელიც 1000'დან 0'მდე დაპრინტავს ყველა რიცხვს

for i in range(1000, -1, -1):
    print(i)


# 4. მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს.
# დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.
age = int(input("Enter your age: "))

if age < 18:
    print("You get a 50% discount!")
else:
    print("You have to pay the full price.")


# 5. მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე და 18 წლის ხალხზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას, 18 წლის ადამიანი მიიღებს 25% ფასდაკლებას
# ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება და თუ მიიღო რამდენი.

age = int(input("Enter your age: "))

if age < 18:
    print("You get a 50% discount!")
elif age == 18:
    print("You get a 25% discount!")
else:
    print("You have to pay the full price.")


# 6 მაღაზიაში ფასდაკლება არის მხოლოდ არასრულოვნებზე და სტუდენტებზე. არასრუწლოვანი ან სტუდენტი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი ან არასტუდენტი გადაიხდის 
# ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")

if age < 18 or is_student.lower() == "yes":
    print("You get a 50% discount!")
else:
    print("You have to pay the full price.")
=======
#1) შექმენით for loop'ი რომელიც 0'დან 200'მდე დაპრინტავს ყოველ მეექვსე რიცხვს

for i in range(0, 201, 6):
    print(i)


#2) გადაატეთ for loop'ი სტრინგს: "Goodbye World!"

string = "Goodbye World!"
for char in string:
    print(char)


#3) შექმენით for loop'ი რომელიც 1000'დან 0'მდე დაპრინტავს ყველა რიცხვს

for i in range(1000, -1, -1):
    print(i)


# 4. მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს.
# დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.
age = int(input("Enter your age: "))

if age < 18:
    print("You get a 50% discount!")
else:
    print("You have to pay the full price.")


# 5. მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე და 18 წლის ხალხზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას, 18 წლის ადამიანი მიიღებს 25% ფასდაკლებას
# ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება და თუ მიიღო რამდენი.

age = int(input("Enter your age: "))

if age < 18:
    print("You get a 50% discount!")
elif age == 18:
    print("You get a 25% discount!")
else:
    print("You have to pay the full price.")


# 6 მაღაზიაში ფასდაკლება არის მხოლოდ არასრულოვნებზე და სტუდენტებზე. არასრუწლოვანი ან სტუდენტი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი ან არასტუდენტი გადაიხდის 
# ჩვეულებრივ ფასს. დაწერე პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.

age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ")

if age < 18 or is_student.lower() == "yes":
    print("You get a 50% discount!")
else:
    print("You have to pay the full price.")
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
