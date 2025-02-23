# colorgram library
import colorgram # type: ignore
from turtle import Turtle,Screen
import turtle

colors= colorgram.extract("image.png")
from random import choice

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = (r,g,b,)
    rgb_colors.append(new_colors)

print(rgb_colors)
color_list = [(202,143,124),(202,193,194),(202,193,114),(215,123,124),(101,213,134),(242,129,204)]
turtle.colormode(255)


mbappe= Turtle()
mbappe.speed("fastest")
mbappe.penup()
mbappe.hideturtle()
mbappe.setheading(225)
mbappe.forward(300)
mbappe.setheading(0)

number_of_dots = 100

for dot_count  in range(1, number_of_dots + 1):
    mbappe.dot(20,choice(color_list))
    mbappe.forward(50)

    if dot_count % 10 == 0:
        mbappe.setheading(90)
        mbappe.forward(50)
        mbappe.setheading(180)
        mbappe.forward(500)
        mbappe.setheading(0)




screen = Screen()
screen.exitonclick()