import turtle

t = turtle.Turtle()

# Square
for i in range(4):
    t.forward(100)
    t.right(90)

# Move
t.penup()
t.goto(150, 0)
t.pendown()

# Circle
t.circle(50)

turtle.done()