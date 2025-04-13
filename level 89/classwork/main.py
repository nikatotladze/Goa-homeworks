# 1

# კომპოზიცია — ძლიერი კავშირი, ნაწილი ვერ ცოცხლობს მთის გარეშე.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  

    def start(self):
        self.engine.start()
        print("Car is ready to go!")

my_car = Car()
my_car.start()


# აგრეგაცია — სუსტი კავშირი, ნაწილი ცოცხლობს დამოუკიდებლად.

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start(self):
        self.engine.start()
        print("Car is ready to go!")

my_engine = Engine()

my_car = Car(my_engine)

my_car.start()


# 2

# ჩვეულებრივი მეთოდია, რომელიც უკავშირდება კონკრეტულ ობიექტს.


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}"

p = Person("nika")
print(p.greet())  


# კლასზე დამოკიდებული მეთოდია და არ საჭიროებს კონკრეტულ ობიექტს.

class Person:
    species = "Human"

    @classmethod
    def info(cls):
        return f"We are {cls.species}s"

print(Person.info())  


# არც ობიექტს და არც კლასს არ საჭიროებს. დამოუკიდებელი ფუნქციაა, უბრალოდ კლასშია მოთავსებული.

class MathHelper:
    @staticmethod
    def add(x, y):
        return x + y

print(MathHelper.add(5, 3))  

# 3

# Multiple Inheritance და Multilevel Inheritance ორივე კონცეფიაა, რომელიც გამოიყენება პროგრამირების ენებში

# 4


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner

        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("მნიშვნელობა უნდა იყოს დადებითი")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("არასაკმარისი თანხა ან არასწორი თანხა")

account = BankAccount("nika", 1000)


print(account.get_balance())  


account.deposit(500)
print(account.get_balance())  


account.withdraw(300)
print(account.get_balance()) 



