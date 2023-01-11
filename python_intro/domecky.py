from turtle import forward
from turtle import right
from turtle import exitonclick
from math import sqrt
from turtle import penup
from turtle import pendown
from random import randint
from turtle import goto


def draw_house(a):
    i = round(sqrt(2*(a**2)))
    b = round(sqrt(2*(1/2*a)**2))
    y=1
    
    right(-90)
    forward(a)
    right(-135)
    forward(i)
    right(135)
    forward(a)
    right(90)
    forward(a)
    right(-135)
    forward(b)
    right(-90)
    forward(b) 
    right(-90)
    forward(i)
    right(135)
    forward(a)
    right(180)

def draw_town(size):
    x =0
    while (x<size):
        draw_house(randint(50, 150))
        penup()
        goto(randint(-400,400), randint(-400,400))
        pendown()
        x = x+1
    
draw_town(666)

exitonclick()
