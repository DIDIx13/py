from turtle import (shape, forward, right, left, speed, exitonclick)

shape("turtle")
speed(0)

def dragon(x, angle=1, n=0):
    if n > 0:
        left(45*angle)
        dragon(2 ** .5 / 2 * x, 1, n -1)
        right(90 * angle)
        dragon(2 ** .5 / 2 * x, -1, n -1)
        left(45*angle)
    else:
        forward(x)
dragon(100,2,10)

exitonclick()
