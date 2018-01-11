from turtle import(shape, backward, forward, left, right, exitonclick, speed)
from turtle import(penup, pendown)

shape("turtle")
speed(0)
x=250
n=0
def maison(x, n):
    toit = 2**.5 / 2* x
    left(90)
    forward(x)
    right(45)
    #toit
    if n >0:
        maison(toit, n -1)
    else:
        forward(toit)
    right(90)
    if n > 0:
        maison(toit, n -1)
    else:
        forward(toit)
        
    right(45)
    forward(x)
    right(135)
    forward(2** .5 * x)
    right(135)
    forward(x)
    right(135)
    forward(2** .5 * x)
    left(135)
    forward(x)
#penup()
#backward(500)
#right(90)
#forward(400)
#left(90)
#pendown()
while 1==1:
    x= x/2
    maison(x, 6)
#maison(500);maison(250);maison(125);maison(62.5);maison(31.25);maison(15.625);maison(15.625);maison(31.25);maison(62.5);maison(125);maison(250);maison(500)
exitonclick()
