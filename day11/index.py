# BLACKJACK GAME
from random import choice
# from replit import clear

# To calculate the score of the user and the computer
def calculate_score(cards):
    # if  len(cards) == 2 and 11 in cards and 10 in cards:
    if  len(cards) == 2 and sum(cards) == 21:
        return 0
    elif 11 in cards  and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    return sum(cards)

# Comparing th euserscore and the computerscore
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"
    
# To deal a card
def deal_card():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    return choice(cards)
def play_game():
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    is_game_over = False

    # DEAL THE CARDS
    # for picking_card in range(2):
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over == False:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)

            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's firstcard: {computer_cards[0]}, current score: {computer_score}")

            # if the user score is 0 or the computer score is 0 or the user score is greater than 21, the game should end
            if user_score == 0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:\
            # else the user should be asked if they want to pick another card
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal == "y":
                    user_cards.append(deal_card())

                else:
                    is_game_over = True

    # if the computer score is less than 17, it should pick another card
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    # clear()
    play_game()
