class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

class Programmer(Human):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language

    def code(self):
        print(f"{self.name} is coding in {self.language}.")

class Designer(Human):
    def __init__(self, name, age, tool):
        super().__init__(name, age)
        self.tool = tool

    def design(self):
        print(f"{self.name} is designing with {self.tool}.")

class Goaprogrammer(Programmer):
    def __init__(self, name, age):
        super().__init__(name, age, "Go")

    def special(self):
        print(f"{self.name} is a Go specialist!")

class Goadesigner(Designer):
    def __init__(self, name, age):
        super().__init__(name, age, "Figma")

    def creative(self):
        print(f"{self.name} is a creative Figma expert!")

class Professional(Programmer, Designer):
    def __init__(self, name, age, language, tool):
        Programmer.__init__(self, name, age, language)
        Designer.__init__(self, name, age, tool)

    def show_skills(self):
        print(f"{self.name} codes in {self.language} and designs with {self.tool}.")

human = Human("Alex", 30)
human.introduce()

prog = Goaprogrammer("John", 25)
prog.introduce()
prog.code()
prog.special()

des = Goadesigner("Emma", 27)
des.introduce()
des.design()
des.creative()

pro = Professional("Sarah", 29, "Python", "Photoshop")
pro.introduce()
pro.show_skills()


# 2

# super() გვჭირდება parent კლასის მეთოდებისა და ატრიბუტების გამოსაძახებლად child კლასში

# 3

# super() აგზავნის გამოძახებას parent კლასში რათა იქ არსებული მეთოდები ან თვისებები გამოვიყენოთ child კლასში


# 4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)  
        self.job_title = job_title  

    def work(self):
        print(f"{self.name} works as a {self.job_title}.")


person = Person("ani", 19)
person.introduce()

employee = Employee("giorgi", 20, "programmer")
employee.introduce()   
employee.work()  
