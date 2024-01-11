import turtle
from turtle import *

speed(0)
bgcolor("black")
setup(400, 250)
penup()
goto(-250, -250)
pendown()

color("yellow")
begin_fill()
forward(600)
left(90)
forward(200)
left(90)
forward(600)
end_fill()

color("blue")
begin_fill()
right(90)
forward(200)
right(90)
forward(600)
right(90)
forward(200)
end_fill()

hideturtle()
turtle.done()
