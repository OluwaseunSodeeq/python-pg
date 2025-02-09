# Randomization
import random
import new_module

# Integer Random number #to generate an interger number
random_interger = random.randint(1,10)
print(random_interger)

# utilizing module
print(new_module.friends)

# floating random number
random_float = random.random()
print(random_float)#to generate  a float number


#Toss coins
head_or_tail = random.randint(1,2)
if head_or_tail == 1:
    print("Head")
else:
    print("Tail")

# List
new_list =  new_module.friends
print(new_list[0])
new_list[2] = "Tope"
print(new_list[-1])


# to add to the end
new_list.append("Geezy")
# to add multiple to the end
new_list.extend(["Sister Nofisat","Mr Akeem"])

# to add to the begining
new_list.insert(0,"Mr Rabiu")
print(new_list)


# my_friends = input("what are ur friends name? ")
my_friends = ['Mr Rabiu', 'Malik', 'Ebuka', 'Tope', 'Geezy', 'Sister Nofisat', 'Mr Akeem']
print(len(my_friends))
lent_List = len(my_friends)

# splitted_list = my_friends.split(", ")
# print(splitted_list)
random_num1 = random.randint(0, lent_List-1)
print(random_num1)
random_friend = my_friends[random_num1]
print(random_friend)
# print(random_friend,randomNum1)

list_result = random.choice(my_friends)
print(list_result)

#ROCK PAPER SCISSORS Game 
list_of_Game = ["ROCK","PAPER","SCISSORS"]
game_on = True

if game_on:

    entered_input = int( input("what do u choose? 0 for Rock, 1 for Scissors, 2 for Paper,  "))
    computer_choice = list_of_Game[ random.randint(0, len(list_of_Game) -1)]

    # def game_function():
    #     users_choice = input("what do u choose? ").upper()
    #     computer_choice = list_of_Game[ random.randint(0,len(list_of_Game) -1)]



    

    if entered_input > len(list_of_Game) -1:
        print("Invalid input")
        print("You lose")
        game_on = False
    else:

        users_choice = list_of_Game[entered_input]

        print(f"Computer chose: {computer_choice}")
        print(f"User chose: {users_choice}")
        if computer_choice == users_choice:
            print("It's a draw")
            game_on = True
            # game_function()
        elif users_choice == "ROCK" and computer_choice == "SCISSORS":
            print("You win")
            game_on = True
            # game_function()
        elif users_choice == "SCISSORS" and computer_choice == "PAPER":
            print("You win")
            game_on = True
            # game_function()
        elif users_choice == "PAPER" and computer_choice == "ROCK":
            print("You win")
            game_on = True
            # game_function()
        else:
            print("You lose")
            print("Game Over")
            game_on = False



# FUNCTIONS that can be used with list are:
# append, extend, insert, remove, pop, clear,
# index, count, sort, reverse, copy,
# chioce, shuffle, randint