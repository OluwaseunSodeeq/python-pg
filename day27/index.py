# import tkinter
# import turtle
from tkinter import *
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# This will keep the window open
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))

# NOTE:
# pack()is used to display the widget in the window to(left,right,top,bottom)
# while place() is used to display the widget in the window to a specific location
# while grid() is used to display the widget in the window to a table like structure


my_label.pack(side="top")
# my_label.pack(side="left")
# my_label.pack(expand=True)

# how to modify the default text
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.place(x=100,y=200)


# for input field
input = Entry(width=40)
input.pack()

# Button

def button_clicked():
    my_label.config(text= f"user input is {input.get()}" )

button  = Button(text="Click Me",command=button_clicked, font=("Arial", 24, "bold"))

button.pack()
button.place(x=0,y=0)
button.config(text="New Button")
button.grid(column=5, row=8)

# button.pack(side="top")
# button.place(x=100,y=200)

# tin = turtle.Turtle()
# tin.write("Hello World", font=("Arial", 24, "bold"))



window.mainloop()

















# Unlimited argument
def add(*args):
    print(args)

    # for n in args:
    #     print(n)
    # OR
    return sum(args)
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# many arguments
# def calculate(n, **kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2, add=3, multiply=5)

# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")
#         self.seats = kwargs.get("seats")


# my_car = Car(make="Royce Roll", model="RR", color="Black", seats=4)