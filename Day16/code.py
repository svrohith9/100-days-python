# OOPS
from turtle import Turtle
from prettytable import PrettyTable

timmy = Turtle()
print(timmy)

my_screen = Screen()
print(my_screen.canvheight)
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(50)

print("*********************************")

# pretty table usage
table = PrettyTable()

table.add_column(fieldname="Pokemon", column=["Pikachu", "Charizard", "Bulbasor"])
table.add_column(fieldname="Type", column=["electric", "fire", "water"])
table.align = 'l'  # left alignment
print(table)
