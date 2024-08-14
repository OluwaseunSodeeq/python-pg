# FUNCTION
import math
def greet():
    print("hi Oluwaseun")

greet()
coverage = 5
def paint_calc(width,height,coverage):
    number_of_can = math.ceil( (width * height) / 5)
    print(f"You will need {number_of_can} cans of paint")




paint_calc(200,0.3,coverage)
paint_calc(9,3,coverage)
paint_calc(3,5,coverage)

def prime_num (num):
    num_checker =  num
    if num_checker <= 1:
        print(f"{num_checker} is a primenumber")
    if num_checker  <= 3:
        print(f"{num_checker} is a primenumber")
    if num_checker  % 2 == 0 or num_checker % 3 == 0:
        print(f"{num_checker} is not a primenumber")
    i = 5
    while i * i <= num_checker:
        print(f"{num_checker} is not a primenumber")
    print(f"{num_checker} is a primenumber")
# prime_num(29)

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

alphabets =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

 # Angela codes
def caesar_cipher (text,shift,direction):
    final_text = ""
    if direction == "decode":
            shift *= -1
    for each_letter in text:
        position = alphabets.index(each_letter)
        new_position = position + shift
        final_text += alphabets[new_position]
    print(f"The {direction}d text is {final_text} ")

continue_playing = True
while continue_playing:
    
    direction = input("Type 'encode' to encrypt,Type 'decode' to decrypt: \n")
    shift=int(input("type the shift number \n"))
    text=input("input your text \n").lower()

    shift = shift % 26
    caesar_cipher(text,shift,direction)
    result = input("Type 'yes' if u want to continue and 'no' if u want to end it \n")
    if result == "no":
        continue_playing = False
        print("Good bye!!!")

   
# =========================================================
# THis didnt work
def decrypt_encrypt_func2(text, shift, direction):
    shifted_text = ""
    for each_letter in text:
        if each_letter in letters:
            position = letters.index(each_letter)
            if direction == "encode":
                position = (position + shift) % len(letters)
            elif direction == "decode":
                position = (position - shift) % len(letters)
            shifted_text += letters[position]
        else:
            shifted_text += each_letter  # If not a letter, add it as is
    
    print(shifted_text)
# THis didnt work
# 
def decrypt_encrypt_func(text,shift,direction):
    print(direction)
    shifted_text = ""
    if direction == "encode":
        print("I am endode")
        for each_letter in text:
            position = letters.index(each_letter) + shift

            if(position > len(letters)):
                position -= len(letters )
                shifted_text += letters[position]
            else:
                shifted_text += letters[position]
        
    elif direction == "decode":
        print("I am decode")
        for each_letter in text:
            position = letters.index(each_letter) - shift

            if(position < 0):
                position = (-1 * position )
                print(position)
                shifted_text += letters[position]
            else:
                shifted_text += letters[position]
    print(shifted_text)




def encrypt(text,shift):
    # text=input("input your text \n")
    print("encode")

    shifted_text = ""
    for each_letter in text:
        position = letters.index(each_letter) + shift

        if(position > len(letters)):
          position -= len(letters )
          shifted_text += letters[position]
        else:
         shifted_text += letters[position]
    print(shifted_text)

def decrypt(text,shift):
    # text=input("input your text \n"
    print("decode")
    shifted_text = ""
    for each_letter in text:
        position = letters.index(each_letter) - shift

        if(position < 0):
          position = (-1 * position )
          shifted_text += letters[position]
        else:
         shifted_text += letters[position]
    print(shifted_text)


print(direction)
# if direction == "encode" or direction == "dedcode":
# caesar_cipher(text,shift,direction)
# if direction == "decode":
#     decrypt(text,shift)
# else:
#     print("Invalid direction. Please type 'encode' or 'decode'.")

