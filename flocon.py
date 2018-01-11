from turtle import (shape, setposition, setheading, heading, position, penup, pendown, speed, forward, left, right, backward, exitonclick)

#shape("turtle")
speed(0)
grammaire = {    
    #"A": "+B-A-B+", # 60° Triangle Sierpinsky
    #"B": "-A+B+A-",

    "A": "+A--B+", # 45° Dragon
    "B": "-A++B-",

    "T": "TT",
    "F": "T[+F]-F",
    "+": "+",
    "-": "-",
    "[": "[",
    "]": "]",
}

def générer(mot, n):
    for i in range(n):
        résultat =""
        for lettre in mot:
            résultat += grammaire[lettre]
        mot = résultat
    return résultat
def dessiner(mot, distance, angle):
    pile=[]
    for lettre in mot:
        if lettre == '+':
            left(angle)
        elif lettre == '-':
            right(angle)
        elif lettre == '[':
            pile.append(
                (position(),heading())
                )
        elif lettre == ']':
            pos, head = pile.pop()
            penup()
            setposition(pos)
            setheading(head)
            pendown()
        else:
            forward(distance)
penup()
backward(500)
right(90)
forward(400)
left(90)
pendown()
dessiner (générer("A", 8), 10, 45)

exitonclick()
