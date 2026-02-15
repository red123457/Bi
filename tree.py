import turtle
tu = turtle.Turtle()
tu.screen.bgcolor("black")
tu.pensize(2)
tu.color("green")
tu.left(90)
tu.backward(100)
tu.speed(0)
tu.shape("turtle")

def tree(i):
	if i < 10:
		return
	else:
		tu.forward(i)
		tu.color("red")
		tu.circle(2)
		tu.color("darkgreen")
		tu.left(30)
		tree(i * 3 / 4)
		tu.right(60)
		tree(i * 3 / 4)
		tu.left(30)
		tu.backward(i)

tree(80)
turtle.done()
