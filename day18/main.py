# Not a good practice to import
# from turtle import *

# Best Practice
from turtle  import Turtle,Screen
import turtle
from random import choice,randint
kylie = Turtle()

# kylie = Turtle()
kylie.shape("turtle")
kylie.color("blue")

# Square
# kylie.forward(100)
# kylie.left(90)
# kylie.forward(100)
# kylie.left(90)
# kylie.forward(100)
# kylie.left(90)
# kylie.forward(100)
# kylie.left(90)

if 2 > 3:
    for _ in range(4):
        kylie.forward(100)
        kylie.left(90)

    for _ in range(14):
        kylie.forward(14)
        kylie.penup()
        kylie.forward(14)
        kylie.pendown()
num_sides = 5
colors = ["red","green","blue","green","purple","yellow","violet","black","pink","indigo"]

if 1 > 2 :
    def draw_shape(num_sides):
        angle = 360 / num_sides
        kylie.forward(100)
        kylie.right(angle)


    # start from 3 and end at 10
    for shape_side_n in range(3, 11):
        kylie.color(choice(colors))
        draw_shape(draw_shape)

directions = [0,90,180,270]
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 225)
    b = randint(0, 255)
    return (r,g,b)


if 3 > 4:
    for _ in range(50):
        kylie.color(random_color())
        kylie.forward(50)
        kylie.setheading(choice(directions))
        kylie.pensize(10)
        kylie.speed("fast")

kylie.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        kylie.color(random_color())
        kylie.circle(100)
        kylie.setheading( kylie.heading() + size_of_gap)

draw_spirograph(5)




screen  = Screen()
screen.exitonclick()
# tuple
# my_tuple = (1,2,3,4,5)






















# # screen  = Screen()from turtle import Turtle, Screen
# from random import choice, randint

# kylie = Turtle()
# kylie.shape("turtle")
# kylie.color("blue")

# def draw_square(size):
#     for _ in range(4):
#         kylie.forward(size)
#         kylie.left(90)

# def draw_shape(num_sides, size):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         kylie.forward(size)
#         kylie.right(angle)

# def random_color():
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return (r, g, b)

# def draw_spirograph(size_of_gap):
#     for _ in range(100):
#         kylie.color(random_color())
#         kylie.circle(100)
#         kylie.setheading(kylie.heading() + size_of_gap)

# def main():
#     colormode(255)
#     kylie.speed("fastest")

#     colors = ["red", "green", "blue", "green", "purple", "yellow", "violet", "black", "pink", "indigo"]
#     directions = [0, 90, 180, 270]

#     for shape_side_n in range(3, 11):
#         kylie.color(choice(colors))
#         draw_shape(shape_side_n, 100)

#     for _ in range(50):
#         kylie.color(random_color())
#         kylie.forward(50)
#         kylie.setheading(choice(directions))
#         kylie.pensize(10)

#     draw_spirograph(10)

#     screen = Screen()
#     screen.exitonclick()

# if __name__ == "__main__":
#     main()