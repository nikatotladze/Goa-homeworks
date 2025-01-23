<<<<<<< HEAD
#1 გაიარეთ sololearn'ი Modulo 4 Quiz'ის ჩათვლით

#გავიარე



# 2) გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

product = 1
for i in range(1, 11):
    product *= i
print("The product of numbers from 1 to 10 is:", product)


# 3) გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

product = 1
i = 1
while i <= 10:
    product *= i
    i += 1
print("The product of numbers from 1 to 10 is:", product)


# 4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:       10 % 2 = 0;        5 % 2 = 1)

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# 5) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ ფოტოს მიხედვით:
# (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)


score = int(input("Enter your score: "))

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
elif 50 <= score <= 59:
    print("Grade E")
else:
    print("Grade F")
=======
#1 გაიარეთ sololearn'ი Modulo 4 Quiz'ის ჩათვლით

#გავიარე



# 2) გამოიყენეთ for loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

product = 1
for i in range(1, 11):
    product *= i
print("The product of numbers from 1 to 10 is:", product)


# 3) გამოიყენეთ while loop'ი და გამოიტანეთ 1'დან 10'ის ჩათვლით რიცხვების ნამრავლი

product = 1
i = 1
while i <= 10:
    product *= i
    i += 1
print("The product of numbers from 1 to 10 is:", product)


# 4) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. (hints:       10 % 2 = 0;        5 % 2 = 1)

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")


# 5) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით მისი grade ამ ფოტოს მიხედვით:
# (ანუ თუ მაგალითად 90'დან 100'ის ჩათვლით ექნება ქულა გამოუტანეთ "Grade A", თუ 80'დან 89'ის ჩათვლით გამოუტანეთ "Grade B" და ა.შ)


score = int(input("Enter your score: "))

score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
elif 50 <= score <= 59:
    print("Grade E")
else:
    print("Grade F")
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
