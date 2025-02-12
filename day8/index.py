# FUNCTION
import math
def greet():
    print("hi Oluwaseun")

greet()

# Function that takes an argument
height_value = int(input("Enter the height of the wall: "))
weight_value = int(input("Enter the weight of the wall: "))

area = weight_value * height_value
coverage = 5

def paint_calc(area, coverage):
    number_of_can = math.ceil( area / coverage)
    print(f"You will need {number_of_can} cans of paint")


paint_calc(area, coverage)

def prime_num (num):
    num_checker =  num
    # if num_checker <= 1:
    #     print(f"{num_checker} is a prime number")
    if num_checker  <= 3:
        print(f"{num_checker} is a prime number")
    if num_checker  % 2 == 0 or num_checker % 3 == 0:
        print(f"{num_checker} is not a prime number")
    i = 5
    while i * i <= num_checker:
        print(f"{num_checker} is not a prime number")
    print(f"{num_checker} is a prime number")
# prime_num(29)

# if any number between 2 and the inputed  number is module by 2 and the remainder is 0, then it is not a prime number
# however, if there is always a remainder, then it is a prime number

def prime_checker(num):
    for i in range(2,num):
        if num % i == 0:
            print(f"{num} is not a prime number")
        else:
            print(f"{num} is  a prime number")
prime_checker(83)


# ===========================================
# Caesar Cipher SOLUTION
letters =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

 # Angela codes
def caesar_cipher (text,shift,direction):
    final_text = ""
    # to change the direction to backward
    if direction == "decode":
            shift *= -1

    for each_char in text:
        if each_char in alphabets:
            position = alphabets.index(each_char)
            new_position = position + shift
            final_text += alphabets[new_position]

        # if the character is not in the alphabets, then it should be left as it is
        else :final_text += each_char
    print(f"The {direction}d text is {final_text} ")

continue_playing = True
while continue_playing:

    direction = input("Type 'encode' to encrypt,Type 'decode' to decrypt: \n")
    shift=int(input("type the shift number \n"))
    text=input("input your text \n").lower()

    # if the user enters a shift that is greater than the number of alphabets, then the shift should be the remainder of the shift divided by 26
    shift = shift % 26

    # call our function
    caesar_cipher(text, shift, direction)

    user_response_to_continue = input("Type 'yes' if u want to continue and 'no' if u want to end it \n")
    
    if user_response_to_continue == "no":
        continue_playing = False
        print("Good bye!!!")

# ===========================================