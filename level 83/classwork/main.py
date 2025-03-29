# 1

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def start_engine(self):
        return f"{self.brand} {self.model} ძრავა ჩაირთო!"

    def car_info(self):
        return f"ავტომობილი: {self.brand} {self.model}, {self.year}, {self.color} ფერი"

car1 = Car("BMW", "M3e46", 2022, "იასამნის")
car2 = Car("merceders", "w204", 2019, "შავი")
car3 = Car("audi", "R8", 2021, "ლურჯი")

print(car1.car_info())
print(car1.start_engine())

print(car2.car_info())
print(car2.start_engine())

print(car3.car_info())
print(car3.start_engine())


# 2

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def full_info(self):
        return f"{self.year} {self.brand} {self.model}"
    
    def is_old(self):
        return "Old" if self.year < 2015 else "New"


car1 = Car("Toyota", "Camry", 2010)
car2 = Car("BMW", "X5", 2020)
car3 = Car("Mercedes", "C-Class", 2018)

for car in (car1, car2, car3):
    print(f"Brand: {car.brand}, Model: {car.model}, Year: {car.year}")
    print(f"Full Info: {car.full_info()}")
    print(f"Condition: {car.is_old()}\n")


# 3

# dunder method - არის phyton ის მეთოდები რომლებიც იწყება და მთავრდება ქვედა ხაზით

# 4

# instance variables - არის ცვლადები რომლებიც დაკავშირებულია კონკრეტულ ობიექტთან

# 5

# Class variables - არის ცვლადები რომლებიც ეკუთვნის მთელ კლასს და ყველა ობიექტს

# 6

# Blueprint - არის კლასის იდეა Python-ში 
