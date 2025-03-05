from random import randint
from collections import Counter
# List comprehension
numbers = [1,2,3,4,5,6,7,8,9]
squared_numbered = [num*num for num in numbers]
print(squared_numbered)

# String
name = "Oluwaseun"
letter_list = [letter for letter in name]
print(letter_list)

# NT: range does not include the last number
range_list = [num * 2 for num in range(1, 11)]
print(range_list)


# Conditional list comprehension
names = ["Alex", "John", "Mary", "Steve", "Seun", "Oluwaseun"]
name_with_e = [name for name in names if "e" in name]
short_names=[name for name in names if len(name) < 5]
list_that_starts_with_s = [name for name in names if name.startswith("S")]
print(name_with_e)
print(short_names)
print(list_that_starts_with_s)


# Form new even number List
even_number = [even for even in range(1, 21) if even % 2 == 0]
print(even_number)

#  ============================
# Dictionary comprehension
# =============================
my_bio = {"name":"Oluwaseun Sodeeq", "age": 27,"hubby":"Software Development"}
# new_bio = {"fav_color": "Blue" for key, value in my_bio.items() if key == "name"}
new_bio = {"fav_color": "Blue" for key, value in my_bio.items()}
print(new_bio)

students_scores = {student: randint(1, 100) for student in names}
passed_students = {student: score for (student, score) in students_scores.items() if score > 50}
print(students_scores)
print(passed_students)

# challenge
# Easy
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = list(sentence)
sentence_list = sentence.split()
print(f"SENTENCE LIST : {sentence_list}")
sentence_dict = {word: len(word) for word in sentence_list}
print(sentence_dict)

# Hard
all_words = "".join(sentence_list).lower()
# 1. approach
# result = Counter(all_words)
# 2. approach
result = {word: all_words.count(word) for word in all_words}
print(result)

# Second Challenge
weather_in_celsius = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24
}

weather_in_fahrenheit = {day: (temp * 9/5) + 32 for (day, temp) in weather_in_celsius.items()}
print(weather_in_fahrenheit)

# with Pandas data
students_data = []
for (index,row) in students_data.iterrows():
    if row.student == "Oluwaseun":
        print(row.index)
        print(row.student)
        print(row.score)
