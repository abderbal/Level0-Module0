import turtle
turtle_1 = turtle.Turtle()


turtle_1.shape('turtle')
turtle_1.speed(4)
turtle_1.color('yellow')
turtle_1.pencolor('white')
turtle_1.begin_fill()
turtle_1.goto(-150, -130)
turtle_1.pencolor('yellow')
turtle_1.goto(0, 200)
turtle_1.goto(150, -130)
turtle_1.goto(-165, 115)
turtle_1.goto(165, 115)
turtle_1.goto(-150, -130)
turtle_1.end_fill()

turtle.done()
