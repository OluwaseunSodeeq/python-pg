# Debugging
# Grace hopper programming pioneer
print("Everyone gets bugs")

# Describe the problem
def my_function():
#   for i in range(1, 21):
  for i in range(1, 21):
    if i == 20:
      print("You got it")

my_function()

# Reproduce the error
from random import randint
dice_ing = ["1","2","3","4","5","6"]
dice_num2 = randint(0,5 )
dice_num = randint(1, 6)
print(dice_ing[dice_num])
print(dice_ing[dice_num2])


# play Computer
year = int(input("what is your year of birth ?"))

# this next line wont run if the input is 1994
# if year > 1980 and year < 1994:

if year > 1980 and year <= 1994:
  print(f"You are a millennium.")
elif year > 1994:
  print(f"You are a Gen Z")
elif year > 2024:
  print(f"You are Gen Alpha")
else:
  print(f"You are an accentor!")

# fix d error in the console and in the text editor before continue
# note that the value is still string and this could cause an error
# age = input("How old are you?")

age = int(input("How old are you?"))
if  age > 18 :
    print(f"You can drive at this age of yours. you are now {age}")

# Print is your friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) the bug is in this line
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

# use a debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    # appending the new item outside the loop
    # b_list.append(new_item)
    # print(b_list) this is the bug it has to return the new list not to print it
    return b_list

mutate_result = mutate([1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(mutate_result)


# Even and Odd Exercise
input_number = int(input("Which number do you want to check?"))
# if input_number % 2 = 0: the bug is in this line (assignment operator)
if input_number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# Exercise 2
# new_year =  input("Enter a year: ") Still a string

leap_year_value = int( input("Enter a year: "))
if leap_year_value % 4 == 0:
    if leap_year_value % 100 == 0:
        if leap_year_value % 400  == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")

# Exercise 3

for number in range(1, 102):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
