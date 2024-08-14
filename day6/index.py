# FUNCTION AND WHILE LOOP
import random
gen_result = ""
init_result = ""
def operation_func(result,range_of_char,each_list):
    for ind in range(1, range_of_char + 1):
        print(f"range_of_char: {range_of_char}")
        result += random.choice(each_list)
        print(result)
    return result
       

gen_result += operation_func(init_result,4,["a","b","d","d","e","t","f","d"])

# print(gen_result)
def turn_left():
    print("left")

def move():
    print("move")

def turn_right():
   turn_left()
   turn_left()
   turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right
    move()
    turn_right
    move()
    turn_left()

# 6 times
number_of_hurdle = 6
for ind in range(number_of_hurdle):
    jump_hurdle()

# =====================1
# #while
while number_of_hurdle > 0:
    jump_hurdle()
    number_of_hurdle -= 1

    # ================2
# if u avnt reached where u were heading  keep going
at_goal = ""
wall_in_front = False
while not at_goal():
# if u av reached the wall Jump if not move
    if wall_in_front():
        jump_hurdle()
    else:
        move()


# =================3
wall_in_right =""
front_in_clear=""
def jump_any_hurdle():
    turn_left
    while wall_in_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_in_clear():
        move()
    turn_left()


while not at_goal():
# if u av reached the wall Jump if not move
    if wall_in_front():
        jump_any_hurdle()
    else:
        move()