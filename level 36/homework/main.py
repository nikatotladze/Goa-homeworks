<<<<<<< HEAD
#1

#1

def rental_car_cost(d):
    daily_rate = 40
    total_cost = d * daily_rate

    if d >= 7:
        total_cost -= 50  # Apply $50 discount
    elif d >= 3:
        total_cost -= 20  # Apply $20 discount

    return total_cost


#2

def quarter_of(month):
    # Calculate the quarter using integer division
    return (month - 1) // 3 + 1


#3

def remove_exclamation_marks(s):
    return s.replace("!", "")


#4

def points(games):
    total_points = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
        # No points for x < y
    return total_points


#5

def get_volume_of_cuboid(length, width, height):
    return length * width * height


#2

def manual_in(element, iterable):
    for item in iterable:
        if item == element:
            return True
    return False
=======
#1

#1

def rental_car_cost(d):
    daily_rate = 40
    total_cost = d * daily_rate

    if d >= 7:
        total_cost -= 50  # Apply $50 discount
    elif d >= 3:
        total_cost -= 20  # Apply $20 discount

    return total_cost


#2

def quarter_of(month):
    # Calculate the quarter using integer division
    return (month - 1) // 3 + 1


#3

def remove_exclamation_marks(s):
    return s.replace("!", "")


#4

def points(games):
    total_points = 0
    for game in games:
        x, y = map(int, game.split(':'))
        if x > y:
            total_points += 3
        elif x == y:
            total_points += 1
        # No points for x < y
    return total_points


#5

def get_volume_of_cuboid(length, width, height):
    return length * width * height


#2

def manual_in(element, iterable):
    for item in iterable:
        if item == element:
            return True
    return False
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
