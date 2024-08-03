# Randomization
import random
import new_module

# Integer Random number
random_interger = random.randint(1,10)
print(random_interger)

# utilizing module
print(new_module.friends)

# floating random number
random_float = random.random()
print(random_float)


#Toss coins
head_or_tail = random.randint(1,2)
if head_or_tail == 1:
    print("Head")
else:
    print("Tail")

# List
new_list =  new_module.friends
print(new_list[0])
new_list[2] = "Tope"
print(new_list[-1])


# to add to the end
new_list.append("Geezy")
# to add multiple to the end
new_list.extend(["Sister Nofisat","Mr Akeem"])

# to add to the begining
new_list.insert(0,"Mr Rabiu")
print(new_list)


my_friends = input("what are ur friends name? ")
print(len(my_friends))
lent_List = len(my_friends)
splitted_list = my_friends.split(", ")
# print(splitted_list)
random_num1 = random.randint(0, lent_List-1)
print(random_num1)
random_friend = my_friends[random_num1]
print(random_friend)
# print(random_friend,randomNum1)

list_result = random.choice(my_friends)
print(list_result)