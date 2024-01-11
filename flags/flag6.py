import turtle
from turtle import  *

speed(1)
bgcolor("black")
setup(600, 250)
penup()
goto(-50,110)
pendown()

color("green")
begin_fill()
right(90)
forward(200)
right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(100)
end_fill()

color("white")
begin_fill()
forward(100)
right(90)
forward(200)
right(90)
forward(100)
end_fill()

right(90)
right(90)
forward(100)

color("orange")
begin_fill()
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()


hideturtle()
turtle.done()
