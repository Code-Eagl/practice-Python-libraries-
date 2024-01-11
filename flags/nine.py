import turtle
from turtle import *
speed(4)
setup(800, 500)
bgcolor("black")


#ehite cross
penup()
goto(-400, -50)
pendown()

color("white")
begin_fill()
forward(800)
left(90)
forward(100)
left(90)
forward(800)
end_fill()

#move to next position
penup()
goto(-100, -250)
pendown()
pendown()

begin_fill()
forward(100)
right(90)
forward(500)
right(90)
forward(100)
end_fill()

#blue cross
penup()
goto(-400, -25)
pendown()

color("midnightblue")
begin_fill()
forward(800)
left(90)
forward(50)
left(90)
forward(800)
end_fill()

#move to next position
penup()
goto(-126, -250)
pendown()

begin_fill()
forward(50)
right(90)
forward(500)
right(90)
forward(50)
end_fill()



turtle.done()
