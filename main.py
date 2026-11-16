from myFunctions import *
from random import *

bigMountains(60)

mountains(60)

for times in range(3):
    crater(randint(-290,-215),randint(215,290))

#trail
bob.width(7)
bob.penup()
bob.goto(-160,-400)
bob.pendown()
bob.color("black","brown")
bob.begin_fill()
for times in range(2):
    bob.left(90)
    bob.forward(220)
    bob.left(90)
    bob.forward(40)
bob.end_fill()

