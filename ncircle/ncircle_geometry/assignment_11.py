import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the speed of the turtle
pen.speed(0)

# Draw the square
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Draw the circle
pen.penup()
pen.goto(0, -50)
pen.pendown()
pen.circle(50)

# Hide the turtle
pen.hideturtle()

# Keep the drawing window open
turtle.done()
