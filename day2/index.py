# Day Two

# Primitive Data type
# STRING
str1 = "Hello"
str2 = "Coders"
print(str1,str2)


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

# Number Chararcters
numChar = len(str(num1))
numChar2 = len(str((num1)))
print(numChar,numChar2)



# type operator
print(type(numChar2))
print(type(str1))
print(type(floatNum))

# Mathematical opeartors
addtn=  1234+234
subtact = 7890-123
divsn = 890/10 # it always return floating number
timess = 234*12
expont = 2**5 #2 in 5 places

print(addtn)
print(subtact)
print(divsn)
print(timess)
print(expont)
# PEMDAS


# Number Manipilaution
roundNum = round(8/3) #round removes all number after the decimal
roundNum = round(8/3,2) #round to  decimal place
floattype = 8/3 #it returns float
format_func =  "{:.2f}".format(floattype)
intType = 8//3 #it returns integer
print(intType)
print(floattype)
print(type (intType))
print(type(floattype))
print(format_func)
print(type(format_func))

# F-String is just like template literal
name= "Oluwaseun Sodeeq"
sscore = 21
age = 26
print(f"My name is {name} ,i scored {21} and I am {age} years old")