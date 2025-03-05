import pandas as pd
nato_phonetics_letters = pd.read_csv("./nato_phonetic_alphabet.csv")
# print(nato_phonetics_letters)
#TODO 1. Create a dictionary in this format:
# nato_phonetics_letters_dict = {letter:code for letter,code in nato_phonetics_letters.iterrows()}
nato_phonetics_letters_dict = {row.letter : row.code for (_,row) in nato_phonetics_letters.iterrows()}
print(f"DICTIONARY  : {nato_phonetics_letters_dict}")




#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("enter a word : ").upper()
user_list = [nato_phonetics_letters_dict[letter]  for letter in user_input]
print(f"LIST : {user_list}")

# print(user_input)
# print(user_list)

