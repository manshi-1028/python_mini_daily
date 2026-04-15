from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
timmy.left(90)
timmy.forward(100)
my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
from prettytable import PrettyTable
table=PrettyTable()
table.add_column=("pokemon mame",['charmender','sqirtel','pickachu'])
table.add_column=("type",["fire","water","electric"])
table.align="l"
print(table)
