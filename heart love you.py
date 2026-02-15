import turtle
import math

def draw_perfect_heart_with_text():
    pen = turtle.Turtle()
    pen.color("#B22222")
    pen.width(5)
    pen.speed(0)

    screen = turtle.Screen()
    screen.bgcolor("black")

    pen.penup()
    pen.goto(0, 70)
    pen.pendown()
    pen.begin_fill()

    for angle in range(360):
        x = 16 * math.sin(math.radians(angle))**3
        y = 13 * math.cos(math.radians(angle)) - 5 * math.cos(2 * math.radians(angle)) - 2 * math.cos(3 * math.radians(angle)) - math.cos(4 * math.radians(angle))
        pen.goto(x * 15, y * 15)  
    pen.end_fill()

    pen.hideturtle()
    
    pen.penup()
    pen.goto(0, -50)
    pen.color("white")
    pen.write("I Love You", align="center", font=("Arial", 30, "bold"))
    
    turtle.done()

draw_perfect_heart_with_text()
