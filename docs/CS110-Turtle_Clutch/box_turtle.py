import turtle
# drawing boxes with a function
t=turtle.Pen()
def boxturtle(xval,yval):
	t.penup()
	t.goto(xval,yval)
	t.pendown()
	t.fillcolor("blue")
	t.pencolor("blue")
	for x in range(4):
		  t.fd(100)
		  t.rt(90)

# boxturtle(0,100)
boxturtle(0,0)
boxturtle(0,10)
boxturtle(0,10)
boxturtle(0,20)
boxturtle(0,30)
boxturtle(0,50)
boxturtle(0,80)