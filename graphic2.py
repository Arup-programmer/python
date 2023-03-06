import turtle
turtle.bgcolor("black")
squary = turtle.Turtle()
squary.speed(500)
for i in range(160):
    for color in ['red','blue','yellow','bisque','purple']:
        squary.pencolor(color)
        squary.forward(i)
        squary.left(60)
        squary.right(12)