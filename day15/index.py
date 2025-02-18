# Python virtual environment:
# venv\Scripts\Activate

# from data import MENU
MENU = {
    "irish coffee": {
        "ingredients": {
            "water": 200,
            "milk": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 100,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 2.5,},
    "cappuccino": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 20,
        },
        "cost": 2.0,},
}
is_on = True
profit = 0

resources = {
    "water" :300,
    "milk" : 500,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        order_ingredient >= resources[item]
        print(f"Sorry there is not enough {item}.")
        return False
    return True

def process_coins():
    # return the total calculator
    print("please insert coins ")
    total =int(input("how many quarter ? ")) * 0.25
    total +=int(input("how many dines ? ")) * 0.10
    total +=int(input("how many nickels ? ")) * 0.05
    total +=int(input("how many quarter pennies ? ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is your change {change}")
        global profit
        profit += drink_cost
        return True

    else:
        print("Sorry that's not enough money. Money is refunded.")
        return False
def make_coffee (drink_name,order_ingredient):
    for each in order_ingredient:
       resources[each]


while is_on:
    choice = input("what would you like to have? (irish coffee, latte, cappuccino) ")
    print(choice)

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")

    elif choice == "latte" or choice == "irish coffee" or choice == "cappuccino":
        drink = MENU[choice]

        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])
            make_coffee()


    #             print(f"Here is your {choice}. Enjoy!")
    #             for item in drink["ingredients"]:
    #                 resources[item] -= drink["ingredients"][item]

    else:
        print("Invalid input")
