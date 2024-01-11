import turtle
from  turtle import  *

speed(1)
bgcolor("black")
setup(400, 250)
penup()
goto(-400, 250)
pendown()

#red ractangle
color("red")
begin_fill()
forward(800)
right(90)
forward(250)
right(90)
forward(800)
end_fill()

color("white")
begin_fill()
left(90)
forward(250)
left(90)
forward(800)
left(90)
forward(250)
end_fill()
hideturtle()
turtle.done()