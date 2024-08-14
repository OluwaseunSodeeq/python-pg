import random

# STEP1
word_List = ["ardvark","babbon", "camel"]
chosen_word = random.choice(word_List)
# print(chosen_word)



# step2
display = ["_"] * len(chosen_word)

# def is_letter_in_word(letter,word):
#     return letter in word

# print(is_letter_in_word(guess,chosen_word)) 
lives = 6
print(chosen_word)
keep_runinig = False
while not keep_runinig:
    guess =  input("guess a letter ").lower()
    for i in range(len(chosen_word)):
     if chosen_word[i] == guess:
        # lives -=1
        display[i] = guess
        # 
        if "_" not in display:
         print("You win!!!")
         print(display)
         keep_runinig = True

        

    if guess not in chosen_word:
       lives -=1
       if lives == 0:
         print("Game Over!!!")
         keep_runinig = True
    
    if lives == 0:
         print(lives)
         print("Game Over!!!")
         keep_runinig = True   


# stages = [
#    "'
#    +---+
#    |    |
#    O    |
#   /|\   |
#   / \   |
#   ======
   
   
# '",
# ]