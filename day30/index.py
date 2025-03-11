# ===============
# ====ERROR====
# ==============

# FileNotFound
with open("file.txt") as file:
    file.read()

# keyError
a_dictionary = {"key": "value"}
value = a_dictionary["no-existence-key"]

# IndexError
fruit_list = ["Apple","Banana","Pear"]
fruit = fruit_list[3]
fruit_1 = fruit_list[0]
print(fruit)


try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["sdfgfds"])

except FileNotFoundError:
    file =  open("a_file.txt", "w")
    file.write("somethings")

except KeyError as error_message:
    print(f"The key {error_message} does not exist")

else:
    content = file.read()
    print(content)
finally:
    # file.close()
    # print("File was closed!")
    # raise KeyError
    raise TypeError("This is an error that i made up")


fruits = ["apple","Pear", "Orange"]

def makepie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")

makepie(1)