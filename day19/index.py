from turtle import Turtle, Screen
from random import randint
turt = Turtle()
screen = Screen()

def move_forwards():
    turt.forward(100)
    print("Turtle moves in 10 spaces ")

screen.listen()
screen.onkey(key="space",fun=move_forwards)


# first Challenge
def move_forward():
    turt.forward(100)

def move_backward():
    turt.backward(100)

def move_right():
    new_heading = turt.heading() - 100
    turt.setheading(new_heading)

def move_left():
    new_heading = turt.heading() + 100
    turt.setheading(new_heading)

def clear():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

# Listening to event
screen.onkey(move_forward,"f")
screen.onkey(move_right,"r")
screen.onkey(clear,"c")

# or using positional augment
screen.onkey(key="l",fun=move_left)
screen.onkey(key="b",fun=move_backward)
# screen.onkey(key="f",fun=move_forward)
# screen.onkey(key="r",fun=move_right)

# second Challenge (Instances and states)
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title="make a bet",prompt="Which turtle will win the race? \n Enter color").lower()
colors = ["red","orange","yellow","green","blue","purple"]
beginning = -150
finished_line = 230
all_turtles =[]

for ind,each_color in enumerate(colors):
    new_turtle =  Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(each_color)
    new_turtle.goto(x= -230, y= beginning + (ind * 50))
    all_turtles.append(new_turtle)
    print(user_bet)

is_race_on = False


if user_bet:
    is_race_on = True

while is_race_on:
    for each_turtle in all_turtles:

        if each_turtle.xcor() > finished_line:
            is_race_on=False
            wining_turtle = each_turtle.pencolor()

            if wining_turtle == user_bet:
                print(f"You have won! {wining_turtle} is the winner")
            else:
                print(f"You have lost!{wining_turtle} is the winner")

        random_distance = randint(0,10)
        each_turtle.forward(random_distance)



screen.exitonclick()