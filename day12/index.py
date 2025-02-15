from random import randint

# SCOPE

# GLOBAL SCOPE
enemies = 1
enemies1 = "skeleton"

def increase_enemies():
    # enemies +=2
    enemies1 = "zombie"
    print(f"enemies inside function: {enemies} and {enemies1}")
    print(f"{enemies} and {enemies1} are global variables")

increase_enemies()
print(f"enemies outside function: {enemies}")

# LOCAL SCOPE
def drink_portion():
    portion_strength = 2
    print(portion_strength)

drink_portion()
# print(portion_strength) returns undefined error

# BlOCK SCOPE


# GLobal Constant
PI = 3.14159
PERCENT =  100

def cal_constant():
    return PERCENT * PI

constant_result = cal_constant()

# GUESS NUMBER ALGORITHM

# Constants
current_attempt = 0
hard_attempt = 5
easy_attempt = 10
level_max_attempt = 0
game_over = False


# Generate random number
guess_number = randint(1, 100)  
# print(f"guessed Number: {guess_number}")

# Guess Function
def guess_number_game(attempt):
    global game_over, current_attempt  # Declare global variables

    while game_over == False:
        user_input = int(input("Enter a number between 1 and 100: "))
        current_attempt += 1

        if guess_number == user_input:
            print(f"You got it right in the {current_attempt} attempt")
            print(f"Guessed Number: {guess_number} is the same as the user input: {user_input}")
            game_over = True
        elif guess_number > user_input:
            print("Too low")
        elif guess_number < user_input:
            print("Too high")
        else:
            print("Invalid input")


        if current_attempt == attempt:
            print("You have exhausted your attempts")
            print("Game Over")
            print(f"Guessed Number: {guess_number}")
            game_over = True

# Level of Difficulty
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if level == "easy":
    level_max_attempt = easy_attempt
    guess_number_game(level_max_attempt)
else:
    level_max_attempt = hard_attempt
    guess_number_game(level_max_attempt)


# Another way of achieving the same result
import random  # Import the random module

# Constants
HARD_ATTEMPT = 10
EASY_ATTEMPT = 5
guess_number2 = random.randint(1, 100)  # Generate random number
# print(f"Guessed Number: {guess_number2}")

# Guess Function
def guess_number_game2(attempt):
    game_over = False  
    current_attempt = 0  

    while not game_over:
        user_input = int(input("Enter a number between 1 and 100: "))
        current_attempt += 1

        if guess_number2 == user_input:
            print("You got it right")
            print(f"Guessed Number: {guess_number2} is the same as the user input: {user_input}")
            game_over = True
        elif guess_number2 > user_input:
            print("Too low")
        elif guess_number2 < user_input:
            print("Too high")
        else:
            print("Invalid input")

        if current_attempt == attempt:
            print("You have exhausted your attempts")
            print("Game Over")
            print(f"Guessed Number: {guess_number2}")
            game_over = True

# Level of Difficulty
# level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


# Mad Cntrol flow
level_max_attempt = EASY_ATTEMPT if level == "easy" else HARD_ATTEMPT
# guess_number_game2(level_max_attempt)
