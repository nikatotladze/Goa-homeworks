# 1

# @abstractmethod არის დეკორატორი, რომელიც გამოიყენება აბსტრაქტულ კლასებში, რათა განსაზღვროს მეთოდი, რომელიც შვილობილმა კლასებმა აუცილებლად უნდა დაამოწმონ (override)


# 2

# 1
class Person:
    pass

# 2

class Person:
    def __init__(self, name):
        self.name = name

# 3

class Person:
    def greet(self):
        print("Hello")

# 4

class Animal:
    def eat(self):
        print("eating")

class Dog(Animal):
    pass

# 5

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")


# 6

class BankAccount:
    def __init__(self):
        self.__balance = 0



# 3

class A:
    def method_a(self):
        print("From A")

class B:
    def method_b(self):
        print("From B")

class C(A, B):
    pass

obj = C()
obj.method_a()  
obj.method_b()  


# 4

class Grandparent:
    def method_gp(self):
        print("Grandparent")

class Parent(Grandparent):
    def method_p(self):
        print("Parent")

class Child(Parent):
    def method_c(self):
        print("Child")

obj = Child()
obj.method_gp()  
obj.method_p()   
obj.method_c()   


# 5

class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent constructor")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  
        self.age = age
        print("Child constructor")

obj = Child("Nika", 15)

