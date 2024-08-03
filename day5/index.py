import random
# LOOP
fruits = ["Apple","Orange","Pear"]
for fruit in fruits:
    print(fruit)


total_num = 0
for num in range(1, 101, 2)  :
    total_num += num
    print(num)
print(total_num)
      
# for even   
total_even  = 0
for num_even in range(1,101,2):
    total_even += num_even
print(total_even)




fizz_buzz_num = 0 
for num_buzz in range(1, 101):
    fizz_buzz_num += num_buzz
    if fizz_buzz_num % 3 == 0 and fizz_buzz_num % 5 == 0:
      print("fizzBuzz")
    elif fizz_buzz_num % 3 == 0:
      print("Fizz")
    elif fizz_buzz_num % 5 == 0:
      print("Buzz")
    else:
       print(num_buzz)
   

    
# PASSWORD GENERATOR
letters = [
  'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
  'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numberss = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbolss = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']


len_of_passwords =  int(input("How long should ur password be ? "))
print(len_of_passwords)
range_of_letters =  int(input("How many letters would u like in your password? "))
print(range_of_letters)
range_of_numbers =  int(input("How many numbers would u like in your password? "))
print(range_of_numbers)
range_of_symbols =  int(input("How many synbolss would u like in your password? "))
print(range_of_symbols)

gen_result = ""
init_result = ""
def operation_func(result,range_of_char,each_list):
  if (range_of_letters + range_of_numbers + range_of_symbols) > len_of_passwords:
     print("your Input length is more than the length of password you specified")
  else:
    for ind in range(1, range_of_char + 1):
        # rdom = random.randint(0,len_of_each_list)
        print(f"range_of_char: {range_of_char}")
        result += random.choice(each_list)
        print(result)
  return result
        # gen_result = result
        # gen_result +=letters[rdom]

gen_result += operation_func(init_result,range_of_letters,letters)
gen_result += operation_func(init_result,range_of_numbers,numberss)
gen_result += operation_func(init_result,range_of_symbols,symbolss)
print(gen_result)
# gen_letter = 

gen_password = f"{gen_result}"

# converting string to List
gen_password_list = list(gen_password)
print(f"Genarate passwordd :{gen_password_list}")
random.shuffle(gen_password_list)
print(f"Shuffled password in list :{gen_password_list}")
stringed_list = "".join(map(str,gen_password_list))
print(f"Stringed the list password  :{stringed_list}")
password_result =  f"in the user password, the letters should be {range_of_letters}, the numbers should be {range_of_numbers} and the symbols length should be {range_of_symbols} \n here is the generated password for you {stringed_list}"
print(password_result)
