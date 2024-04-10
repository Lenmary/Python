from turtle import *
import random

colors= ["black","red"]
#bgcolor= "blue"

speed (100)
for x in range (200):
    aleatorio= random.randrange(0,2)
    pencolor(colors[aleatorio])
    width(x/50+1)
    #forward (x)
    circle(100)
    left(70)

hideturtle()
done()