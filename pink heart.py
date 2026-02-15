import math
from turtle import *
def heart(h):
    return 15*math.sin(h)**3

def heart1(h):
    return 12*math.cos(h)-5*\
    math.cos(2*h)-2*\
    math.cos(3*h)-\
    math.cos(4*h)

speed(100)
bgcolor('black')
for i in range(600):
    goto(heart(i)*20 , heart1(i)*20)
    for j in range(5):
        color('hot pink')

done()
