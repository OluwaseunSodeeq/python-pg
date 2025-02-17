# My Solutuion for Day 14 of 100 days of code
from data import celebrities 
from random import choice

game_over = False
lives = 3

while not game_over:
    gen_celeb_list = []

    for i in range(2):
        gen_celeb_list.append(choice(celebrities))

    print(f"Between A = {gen_celeb_list[0]['name']} and B = {gen_celeb_list[1]['name']}")
    # print(f"A = {gen_celeb_list[0]['Instagram followers']}M B = {gen_celeb_list[1]['Instagram followers']}M")

    # User input
    user_choice = input("Who has more followers? 'A' or 'B': ").upper()
    if user_choice == "A":
        user_choice = 0
    elif user_choice == "B":
        user_choice = 1
    else:
        print("Invalid input, please enter 'A' or 'B'")
        continue

    # Determine the correct answer
    if gen_celeb_list[0]["Instagram followers"] > gen_celeb_list[1]["Instagram followers"]:
        correct_choice = 0
        celeb_with_highest_followers = gen_celeb_list[0]
    else:
        correct_choice = 1
        celeb_with_highest_followers = gen_celeb_list[1]

    # Check user input
    if user_choice == correct_choice:
        print(f"You are correct! {celeb_with_highest_followers['name']} has more followers.")
    else:
        lives -= 1
        print(f"You are wrong! {celeb_with_highest_followers['name']} has more followers.")
        print(f"You lost a life. You have {lives} lives left.")
        if lives == 0:
            print("Game over")
            game_over = True


# angela's solution = """

def format_data(account):
    account_name = account['name']
    account_followers = account["Instagram followers"]
    return (f"{account_name} has {account_followers}")

def check_answers(guess, a_followers, b_followers):

    if a_followers > b_followers:
        return guess == "A"
        
    else:
        return guess ==  "B"

attempts = 3
score = 0
game_should_continue = True
account_b = choice(celebrities)


while game_should_continue:
    account_a = account_b
    account_b = choice(celebrities)

    if account_a == account_b:
        account_b = choice(celebrities)
    print(f"Compare A: {format_data(account_a)} VS B: {format_data(account_b)}")

    guess = input("who has more followers 'A' or 'B' ").upper()

    a_followers =  account_a["Instagram followers"]
    b_followers =  account_b["Instagram followers"]

    is_correct =  check_answers(guess, a_followers, b_followers)
    # clear()
    print(is_correct)
    if is_correct:
        print("You are right")
        score += 1
    else:
        print("Sorry, u are wrong!")
        attempts -= 1

        if attempts == 0:
            game_should_continue = False
            print("Game Over!")