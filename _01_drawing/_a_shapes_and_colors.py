import turtle


window = turtle.Screen()
window.bgcolor('white')

# # # This code makes a new Turtle. Pick a new name for the turtle
derin = turtle.Turtle()

# Make your turtle's shape 'turtle', .shape('turtle')
derin.shape('turtle')
# Set your turtle's speed using .speed(2)
derin.speed(10.4)
# Set your turtle's color using .color('green') and .pencolor('blue')
derin.color('blue')
derin.pencolor('black')
# Move your turtle forward using .forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
# Now put the forward and left/right code into a for loop to repeat 4 times.
# TEST    Did your turtle draw a square?
derin.begin_fill()
for i in range (4) :
    derin.forward(200)
    derin.right(90)
derin.end_fill()
# Move your turtle to a new place on the screen using .goto(x, y)
# x=0 and y=0 is the center of the screen
derin.goto(0, 0)
# Have your turtle draw a circle using .circle(radius, steps=30)
# TEST    Did your turtle draw a circle?
derin.begin_fill()
derin.circle(200, steps=50)
derin.end_fill()

derin.begin_fill()
for i in range (4) :
    derin.right(90)
    derin.forward(200)
derin.end_fill()
derin.pencolor ('blue')
derin.goto (80, 80)
derin.pencolor ('black')
derin.goto(50, 45)
derin.goto(10, 35)
derin.goto(-10, 35)
derin.goto(-50, 45)
derin.goto(-80, 80)
derin.pencolor ('blue')
derin.goto(80, 200)
derin.pencolor('black')
derin.begin_fill()
derin.color('white')
derin.circle(27.5, steps=30)
derin.end_fill()
derin.begin_fill()
derin.color('black')
derin.circle(20, steps=30)
derin.end_fill()
derin.color('blue')
derin.goto(-80, 200)
derin.pencolor('black')
derin.begin_fill()
derin.color('white')
derin.circle(27.5, steps=30)
derin.end_fill()
derin.begin_fill()
derin.color('black')
derin.circle(20, steps=30)
derin.end_fill()
derin.pencolor('blue')
derin.goto(80, 80)
derin.pencolor('black')
derin.goto(50, 67.5)
derin.goto(10, 55)
derin.goto(-10, 55)
derin.goto(-50,67.5)
derin.goto(-80, 80)
derin.color('blue')
derin.pencolor('blue')
derin.goto(-100, 80)
derin.goto(0, 175)
derin.pencolor('black')

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below

# Draw 3 more shapes with different fill colors!

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
