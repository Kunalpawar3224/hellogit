import turtle
import tkinter as tk

# Draw the square
def draw_square():
    t = turtle.Turtle()
    t.penup()
    t.goto(-50, -50)  # Starting point of the square
    t.pendown()
    t.pensize(2)
    for _ in range(4):
        t.forward(100)  # Length of each side of the square
        t.left(90)
    t.hideturtle()

# Draw the inscribed circle
def draw_circle():
    t = turtle.Turtle()
    t.penup()
    t.goto(0, -50)  # Center point of the circle
    t.pendown()
    t.circle(50)  # Radius of the circle
    t.hideturtle()

# Create the Tkinter window
window = tk.Tk()

# Create the buttons
start_button = tk.Button(window, text="Start")
stop_button = tk.Button(window, text="Stop")
pause_button = tk.Button(window, text="Pause")

# Set the layout using the grid system
start_button.grid(row=0, column=0)
stop_button.grid(row=0, column=1)
pause_button.grid(row=0, column=2)

# Adjust the spacing between buttons
window.grid_columnconfigure(1, minsize=100)  # Space between Start and Stop buttons
window.grid_columnconfigure(2, minsize=100)  # Space between Stop and Pause buttons

# Call the functions to draw the square and inscribed circle
draw_square()
draw_circle()

# Run the Tkinter event loop
window.mainloop()

# Close the turtle graphics window
turtle.done()
