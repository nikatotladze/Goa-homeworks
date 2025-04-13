# 1

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(dog.speak()) 
print(cat.speak())  



# 2

class Bird:
    def speak(self):
        return "chit"

class Cow:
    def speak(self):
        return "Moo"

class Human:
    def speak(self):
        return "Hello"

def make_sound(creature):
    print(creature.speak())

make_sound(Bird())   
make_sound(Cow())    
make_sound(Human())  


# 3

# Abstract Class - იყენებს ABC კლასს და @abstractmethod დეკორატორს
# Polymorphism	- 	ყველა ობიექტს აქვს ერთსა და იმავე სახელის მქონე მეთოდი (მაგ. speak()).

