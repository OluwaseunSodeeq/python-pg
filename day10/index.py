# Function And Recursion with output
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year %400  == 0:
                return True
            else:
                False
        else:
            True
    else:
        False

def days_in_month(year,month):
    if month > 12 or month < 1:
        return "Invalid month input"
    
    month_days =[31,28,31,30,31,30,31,31,30,31,30,31,]
    if is_leap(year) and month == 2:
       return 29
    
    return month_days[month - 1]
    


year = int(input("Enter a year:  "))
month = int(input("Enter a month:  "))
days = days_in_month(year,month)
print(days)

# ======================================
# CALCULATOR OPEARATIONS
# ======================================
def add_num(n1,n2):
    return n1 + n2

def subtract_num(n1,n2):
    return n1 - n2

def multiply_num(n1,n2):
    return n1 * n2

def divide_num(n1,n2):
    return n1 / n2


operations = {"+":add_num,"-":subtract_num,"*":multiply_num,"/": divide_num }


# Declaration and Definition of Variables in Python
current_user = "Oluwaseun"

# Declaration and Definition of Functon in Python
def calculator():
    num1 = float(input("What is your first Number"))
    for operator in operations:
        print(operator)

    should_continue = True

    while should_continue:
        operator_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What is your next Number"))
        users_operation_function = operations[operator_symbol]
        answer = users_operation_function(num1,num2)

        print(f"{num1} {operator_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: " ) == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()


    # operation_symbol = input("Pick another operation: ")
    # num3 = int(input("what is the next number?: "))
    # calculation_function = operations[operator_symbol]
    # answer = calculation_function(calculation_function(num1,num3),nu)

    # print(f"{num3} {operator_symbol} {answer1} = {answer}")

# some functions on strings
# title() - capitalize the first letter of each word