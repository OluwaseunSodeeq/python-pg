# OOP
# Constructing and accessing OOP
from turtle import Turtle, Screen
# timmy in the below code is the object and Turtle is the Class or Blueprint 
timmy = Turtle()
timmy.color("blue")
timmy.shape("turtle")
timmy.forward(100)
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# for Packages check the below links
# https://docs.python.org/3/py-modindex.html
# https://pypi.org/
from  prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokenon Name",["Pikachu","Squirtle","Charnander"])
table.add_column("Type",["Electric","Water","Fire"])
print(table)

# align attribute
table.align =  "l"



