import turtle

# Draw a rectangular button with a label
def draw_button(label):
    t = turtle.Turtle()
    t.penup()
    t.goto(-60, 0)  # Starting point of the button
    t.pendown()
    t.fillcolor("gray")
    t.begin_fill()
    for _ in range(2):
        t.forward(120)  # Width of the button
        t.left(90)
        t.forward(30)   # Height of the button
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-50, 10)  # Position the turtle to write the label
    t.write(label, align="center", font=("Arial", 14, "bold"))
    t.hideturtle()

# Create the turtle graphics window
window = turtle.Screen()

# Set up the turtle window size and background color
window.setup(width=500, height=200)
window.bgcolor("white")

# Calculate the spacing between buttons
spacing = 40

# Draw the buttons with labels
draw_button("Start")
draw_button("Stop")
draw_button("Pause")

# Adjust the spacing between buttons
turtle.penup()
turtle.goto(0, -30)
turtle.pendown()

# Draw the spacing line between Start and Stop buttons
turtle.forward(spacing)
turtle.penup()
turtle.goto(spacing, -30)
turtle.pendown()

# Draw the spacing line between Stop and Pause buttons
turtle.forward(spacing)

# Close the turtle graphics window
turtle.done()
