import turtle
from turtle import *

speed(0)
setup(800, 500)
bgcolor("black")
goto(-400, -250)

color("red")
begin_fill()
for i in range(2):
    forward(800)
    left(90)
    forward(250)
    left(90)
end_fill()

penup()
goto(0, -125)
penup()

color("yellow")
begin_fill()
circle(125)
end_fill()

hideturtle()
turtle.done()