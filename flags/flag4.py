import turtle
from turtle import *

speed(1)
bgcolor("black")
setup(600, 250)
penup()
goto(-200,0)
pendown()

color("yellow")
begin_fill()
forward(400)
right(90)
forward(70)
right(90)
forward(400)
right(90)
forward(70)
end_fill()

color("blue")
begin_fill()
right(90)
forward(400)
left(90)
forward(70)
left(90)
forward(400)
left(90)
forward(70)
end_fill()


hideturtle()
turtle.done()
