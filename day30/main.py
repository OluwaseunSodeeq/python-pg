facebook_post =[
{"likes": 21,"Comments":2},
{"likes": 12,"Comments":2,"shares":1},
{"likes": 21,"Comments":4},
{"likes": 21,"Comments":2,'shares':3},
{"likes": 33,"Comments":8},
{"likes": 19,"Comments":3}

]

total_likes= 0

for post in facebook_post:
    try:
       total_likes = total_likes + post["likes"]
    except KeyError:
       total_likes+= 0

print(f"TOTAL LIKES: {total_likes}")



# ===============================
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()