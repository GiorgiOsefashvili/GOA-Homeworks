from turtle import *

#we want to paint a house

#step 1: draw a square

width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing window

penup()
goto(150, 150)
pendown()

width(5)
color("brown")
begin_fill()
left(30)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

left(90)
forward(30)

penup()
forward(100)
pendown()

left(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)

right(90)
forward(30)
end_fill()

exitonclick()