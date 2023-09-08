import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colors = ['red','yellow','blue','green','orange','white']
namez = ["bluey","bingo","bandit","chilli","trixie"]
for x in range(100):
    t.pencolor(colors[x%6])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(namez[x%len(namez)],font=("Arial",int((x+4)/4),"bold"))
    t.left(92)
