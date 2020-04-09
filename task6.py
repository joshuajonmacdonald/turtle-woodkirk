import turtle

turtle.pencolor("cyan")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(5):
    turtle.forward(100)
    turtle.right(72)
turtle.end_fill()
turtle.Screen().exitonclick()
