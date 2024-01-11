import turtle
from turtle import *

speed(0)
bgcolor("black")
setup(400, 250)
penup()
goto(-200, -250)
pendown()

color("red")
begin_fill()
forward(400)
left(90)
forward(200)
left(90)
forward(400)
end_fill()

color("white")
begin_fill()
right(90)
forward(200)
right(90)
forward(400)
right(90)
forward(200)
end_fill()

hideturtle()
turtle.done()
