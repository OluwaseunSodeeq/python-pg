# Day Two

# Primitive Data type

# STRINGS
str1 = "Hello"
str2 = "Coders"
print(str1,str2) 
print(str1 + " " +str2)


# Intergers: number with no decimal
num1 =  1234
numStr =  "1234"
num2 =  1234 + 56789
print(num1, num2)
print(type (int(numStr)))

# Float: with decimal
floatNum = 123.34
print(float)

# Boolean
print(True, False)

# Number Chararcters ==>>  i.e to calculate the length of  a variable
numChar = len(str(num1))
numChar2 = len(str((num1)))
print(numChar,numChar2)



# type operator
print(type(numChar2))
print(type(str1))
print(type(floatNum))

# Mathematical operators
addtn=  1234 + 234
subtact = 7890 - 123
divsn = 890 / 10 # it always return floating number
timess = 234 * 12
expont = 2**5 #2 in 5 places

print(addtn)
print(subtact)
print(divsn)
print(timess)
print(expont)
# PEMDAS From Left to Right

# Number Manipilaution
roundNum = round(8/3) #round removes all number after the decimal
roundNum = round(8/3,2) #round to  decimal place
floattype = 89876/3 #it returns float
format_func =  "{:.2f}".format(floattype)
intType = 8//3 #it returns integer, // is called flow division
print(intType)
print(floattype)
print(type (intType))
print(type(floattype))
print(format_func)
print(type(format_func))

# F-String is just like template literal(for mixing string and other data types)
# it is used for formatting the string

name= "Oluwaseun Sodeeq"
sscore = 21
age = 26
print(f"My name is {name} ,i scored {21} and I am {age} years old")

# Exercise
highest_age = 90
current_age = int(input("What is your current age? "))
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

user_years_left = highest_age - current_age
user_months_left = user_years_left * months_in_year
user_weeks_left = user_years_left * weeks_in_year
user_days_left = user_years_left * days_in_year

users_result = f"You have {user_days_left} days,{user_weeks_left} weeks, {user_months_left} months and {user_years_left} years left"
print(users_result)

# NOTES:
name[0] #subscripting the first chararcter

# Methods
len("ade")
type()
str()
float()
int()
round(floattype, 2) #round to 2 decimal places
 
#the best decimal formater logic
format_function =  "{:.2f}".format(floattype)


# EXAMPLES ON VARIABLES, SCOPES, AND NAMING CONVENTIONS

# VARIABLES AND NAMING CONVENTIONS
user_name = "Oluwaseun"

# GLOBAL VARIABLE
total_price = 100

# LOCAL VARIABLE
def local_scope_example():
    local_var = "I am a local variable"
    print(f"{local_var} will cause a NameError if accessed outside this function. \n {user_name}")
    print(f" and {total_price} can be accessed anywhere in the code.")

# ENCLOSING VARIABLE
def enclosing_scope_example():
    enclosing_var = "I am an enclosing variable"
    def nested_code():
        print(f"{enclosing_var} can be accessed within this enclosing function and its nested function.") 

# BUILT-IN VARIABLE: Using a built-in function
number_list = [1, 2, 3, 4, 5]
total = sum(number_list)  
print(total)
