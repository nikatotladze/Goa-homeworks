from abc import ABC, abstractmethod

# 1 

# ABSTRACT CLASS - აბსტრაქტული კლასი არის კლასი, რომელიც არ შეიძლება პირდაპირ შეიქმნას,
# მას აქვს აბსტრაქტული მეთოდ(ები) და გამოიყენება ბაზისური კლასივით, რომელსაც შვილი კლასები იყენებენ.


# 2 

# POLYMORPHISM - პოლიმორფიზმი ნიშნავს იმას, რომ სხვადასხვა ობიექტებს (Dog, Cat)
# შეიძლება ჰქონდეთ ერთი და იგივე მეთოდი (make_sound), მაგრამ სხვადასხვა ქცევა


# 3 

# AGGREGATION - აგრეგაცია არის ურთიერთობა ობიექტებს შორის, სადაც ერთი ობიექტი შეიცავს მეორეს
# მაგრამ ეს დამოკიდებულება სუსტია - ერთი ობიექტის განადგურება მეორეზე არ იმოქმედებს


# 4

class Animal(ABC):  
    @abstractmethod
    def make_sound(self): 
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# 5

def animal_sound(animal: Animal):
    print(animal.make_sound())  



# 6


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Animal):
        self.pets.append(pet)

    def list_pets(self):
        for pet in self.pets:
            print(f"{self.name}'s pet says: {pet.make_sound()}")



dog = Dog()
cat = Cat()


animal_sound(dog) 
animal_sound(cat) 


owner = Owner("Giorgi")
owner.add_pet(dog)
owner.add_pet(cat)
owner.list_pets()

