import turtle
bob=turtle.Turtle()
bob.speed(0)
turtle.bgcolor("darkblue")
from random import *

#to make bigger mountains function randomly
def bigMountains(angle):
    bob.penup()
    bob.goto(-350,-180)
    bob.pendown()
    bob.color("black","darkgray")
    bob.begin_fill()

    for times in range(3):
        dist=randint(350,450)
        bob.left(angle)
        bob.forward(dist)
        bob.right(angle*2)
        bob.forward(dist)
        bob.left(angle)
    bob.end_fill()
    
#to make mountains function randomly
def mountains(angle):
    bob.penup()
    bob.goto(-350,-180)
    bob.pendown()
    bob.color("black","gray")
    bob.begin_fill()
    for times in range(5):
        dist=randint(200,300)

        bob.left(angle)
        bob.forward(dist)
        bob.right(angle*2)
        bob.forward(dist)
        bob.left(angle)

    bob.goto(-350,-180)
    bob.end_fill()
#makes the grassland
bob.penup()
bob.goto(-480,-180)
bob.pendown()
bob.color("green")
bob.begin_fill()
for times in range(4):
    bob.forward(1000)
    bob.right(90)
bob.end_fill()


#pond
bob.goto(250,-490)
bob.width(4)
bob.color("lightskyblue","lightblue")
bob.begin_fill()
bob.circle(100)
bob.end_fill()

# function to make moon and it's craters
bob.penup()
bob.goto(-250,200)
bob.pendown()
bob.color("white")
bob.begin_fill()
bob.circle(70)
bob.end_fill()


def crater(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    bob.color("lightgray")
    bob.begin_fill()
    bob.circle(15)
    bob.end_fill()



