import turtle
from turtle import  *

speed(0)
bgcolor("black")
setup(600, 250)
penup()
goto(-200,-30)
pendown()

color("red")
begin_fill()
right(90)
forward(70)
left(90)
forward(400)
left(90)
forward(70)
left(90)
forward(400)
end_fill()

color("white")
begin_fill()
right(90)
forward(70)
right(90)
forward(400)
right(90)
forward(70)
end_fill()

color("red")

right(90)
forward(400)
right(90)
forward(70)
begin_fill()
forward(70)
right(90)
forward(400)
right(90)
forward(70)
end_fill()


hideturtle()
turtle.done()