from data import MENU,store

# print(store)
# print(MENU)
should_continue = True
# go_again = True
current_resources = store
available_stock = store

all_menu = []
for each in MENU:
    all_menu.append(each)

print(f"Welcome to OS cafe \n Select from our menu \n ")

while should_continue:
    print(f"{', '.join(all_menu)}")
    user_coffee = input("what coffee would u like to have ???").strip().lower()
    # coffee_to_prepare = user_coffee

    print(user_coffee in MENU)

    if user_coffee == "off":
        print("Machine is under maintenance , try again Later ")
        should_continue = False
    elif user_coffee == "report":
        print(available_stock)
        continue

    elif user_coffee in MENU:
        # User money
        coffee_cost = MENU[user_coffee]['cost']
        print(f"You selected {user_coffee} and its cost #{coffee_cost}")
        user_coffee_cost = int(input("Please make payment ???"))

        print(f"{user_coffee}, its ingredients:{MENU[user_coffee]['ingredients']}")
        user_ingredients = MENU[user_coffee]['ingredients']

        if user_coffee_cost >= coffee_cost:

            for each_ingredient in user_ingredients:
                ingredient = each_ingredient
                quantity = user_ingredients[each_ingredient]
                print(f"{ingredient} Available Quantity: {available_stock[ingredient]['quantity']}")
                available_stock[ingredient]['quantity'] -= quantity
                print(f"{ingredient} Balance Quantity: {available_stock[ingredient]['quantity']}")

            print(f"{user_coffee.capitalize()} is available! It costs #{MENU[user_coffee]['cost']}.")


        else:
            print("Insufficient funds , try again Later ")
            print(f"Sorry, {user_coffee} cost #{coffee_cost}")
            try_again_now = input("Do u want to try again now? type 'Yes'to continue and 'No' to exit ").lower()
            if not try_again_now == "no":
                should_continue= False



    else:
        print("Sorry, that coffee is not on the menu.")
        try_again_now = input("Do u want to try again now? type 'Yes'to continue and 'No' to exit ").lower()
        if not try_again_now == "no":
                should_continue= False

