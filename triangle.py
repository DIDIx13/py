from turtle import (shape, forward, right, left, speed, backward, exitonclick, penup, pendown)


shape("turtle")
speed(0)

def triangle(x = 100, n =0):
    for i in range(3):
        if n > 0:
            triangle(x/2, n - 2)
        forward(x)
        left(120)
penup()
backward(500)
right(90)
forward(400)
left(90)
pendown()
triangle(10000,20)

exitonclick()
