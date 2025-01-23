<<<<<<< HEAD
#1

#1

def rps_game(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

# Examples
print(rps_game("scissors", "paper"))  # Output: "Player 1 won!"
print(rps_game("scissors", "rock"))   # Output: "Player 2 won!"
print(rps_game("paper", "paper"))     # Output: "Draw!"



#2

def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# Examples
print(is_divisible(3, 1, 3))  # True: 3 is divisible by 1 and 3
print(is_divisible(12, 2, 6))  # True: 12 is divisible by 2 and 6
print(is_divisible(100, 5, 3))  # False: 100 is not divisible by 3
print(is_divisible(12, 7, 5))  # False: 12 is neither divisible by 7 nor 5


#3

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

# Examples
print(count_sheep(3))  # Output: "1 sheep...2 sheep...3 sheep..."
print(count_sheep(0))  # Output: ""


#4

def get_grade(s1, s2, s3):
    # Calculate the average score
    average = (s1 + s2 + s3) / 3
    
    # Determine the letter grade
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'


#5

def greet(name, owner):
    # Check if name matches owner
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
=======
#1

#1

def rps_game(player1, player2):
    if player1 == player2:
        return "Draw!"
    elif (player1 == "rock" and player2 == "scissors") or \
         (player1 == "scissors" and player2 == "paper") or \
         (player1 == "paper" and player2 == "rock"):
        return "Player 1 won!"
    else:
        return "Player 2 won!"

# Examples
print(rps_game("scissors", "paper"))  # Output: "Player 1 won!"
print(rps_game("scissors", "rock"))   # Output: "Player 2 won!"
print(rps_game("paper", "paper"))     # Output: "Draw!"



#2

def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0

# Examples
print(is_divisible(3, 1, 3))  # True: 3 is divisible by 1 and 3
print(is_divisible(12, 2, 6))  # True: 12 is divisible by 2 and 6
print(is_divisible(100, 5, 3))  # False: 100 is not divisible by 3
print(is_divisible(12, 7, 5))  # False: 12 is neither divisible by 7 nor 5


#3

def count_sheep(n):
    return ''.join(f"{i} sheep..." for i in range(1, n + 1))

# Examples
print(count_sheep(3))  # Output: "1 sheep...2 sheep...3 sheep..."
print(count_sheep(0))  # Output: ""


#4

def get_grade(s1, s2, s3):
    # Calculate the average score
    average = (s1 + s2 + s3) / 3
    
    # Determine the letter grade
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'


#5

def greet(name, owner):
    # Check if name matches owner
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"
>>>>>>> 078f87372618cabe97856ddd7e397bf9bf3f8892
