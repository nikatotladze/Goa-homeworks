#1

numbers = [x for x in range(1, 101)]
print(numbers)


#2

odd_numbers = [x for x in range(1, 101, 2)]
print(odd_numbers)


#3

names = ["Ana", "Mate", "Saba", "nia", "Lika"]
filtered_names = ["#" + name for name in names if "a" not in name.lower()]
print(filtered_names)

#4

def greet(name):
    # ვამოწმებთ, თუ სახელი არის "Johnny"
    if name == "Johnny":
        return "Hello, my love!"  # სპეციალური მისალმება "Johnny"-სთვის
    else:
        return "Hello, {}!".format(name)  # ჩვეულებრივი მისალმება სხვებისთვის


#5

def update_light(current):
    # ვამოწმებთ მიმდინარე ფერს და ვაბრუნებთ შემდეგ ფერს
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"


