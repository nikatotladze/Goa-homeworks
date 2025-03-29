# 1

class Motorcycle:
    total_motorcycles = 0  

    def __init__(self, brand, model, engine_capacity, color):
        self.brand = brand
        self.model = model
        self.engine_capacity = engine_capacity
        self.color = color
        Motorcycle.total_motorcycles += 1  

bike1 = Motorcycle("ninja", "kavazaki", 1000, "black")
bike2 = Motorcycle("yamaha", "R1", 900, "Red")

print(Motorcycle.total_motorcycles) 


# 2

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "bark")
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "meow")
        self.color = color

class Bird(Animal):
    def __init__(self, name, wing_span):
        super().__init__(name, "chirp")
        self.wing_span = wing_span

dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")
bird = Bird("Tweety", 25)

print(dog.make_sound())  
print(cat.make_sound())  
print(bird.make_sound())  


# 3

# inheritance საშუალებას გვაძლევს, რომ ბაზის (მშობელი) კლასი შექმნათ და მისგან შვილობილი კლასები გამოყოთ


# 4

# Inheritance საჭიროა მაშინ, როცა კოდში გვაქვს საერთო მახასიათებლები და გვინდა, რომ კოდი უფრო ორგანიზებული, მოქნილი და გამეორების გარეშე იყოს

# 5

# Multiple Inheritance არის სიტუაცია, როდესაც ერთი კლასი ერთზე მეტი მშობელი კლასისგან იღებს მემკვიდრეობას.