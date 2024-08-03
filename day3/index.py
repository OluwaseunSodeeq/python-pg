# CONtROL FLOW

# if and ELSE
print("CONTROL FLOW")
# height_val =  int(input("What is your height? "))
height_val =  130
if height_val > 120:
 print("You can ride!!!")
else:
 print("You cannot ride!")

#  Modulo Operation
if 7%2 == 0:
 print("It is even")
else:
 print("It is oods")
 

#  COntrol FLow
# num_to_check =  int(input("enter any number"))
num_to_check =  99
if num_to_check % 2 == 0:
 print(f"The entered number ({num_to_check}) is even")

elif num_to_check % 2 == 1:
 print(f"The entered number ({num_to_check}) is odd")
else:
 print(f"The entered number is neither even nor odd")


# Leap Year chercker
# inputed_year = int(input("what is your year"))
inputed_year = 2021
if inputed_year % 4 != 0 and inputed_year % 100 != 0 and inputed_year % 400 != 0:
 print(f"It is not a leap year")
else:
 print(f"It is a leap year")