# import turtle

# # Function to draw a rectangular button
# def draw_button(x, y, width, height, label):
#     pen.penup()
#     pen.goto(x, y)
#     pen.pendown()
#     pen.fillcolor("gray")
#     pen.begin_fill()
#     for _ in range(2):
#         pen.forward(width)
#         pen.right(90)
#         pen.forward(height)
#         pen.right(90)
#     pen.end_fill()
#     pen.penup()
#     pen.goto(x + width/2, y + height/2)
#     pen.write(label, align="center", font=("Arial", 12, "bold"))

# # Create a turtle object
# pen = turtle.Turtle()

# # Set the speed of the turtle
# pen.speed(0)

# # Set the initial position
# x = -200
# y = 0

# # Draw the "Start" button
# draw_button(x, y, 100, 50, "Start")

# # Update the position
# x += 150

# # Draw the "Stop" button
# draw_button(x, y, 100, 50, "Stop")

# # Update the position
# x += 150

# # Draw the "Pause" button
# draw_button(x, y, 100, 50, "Pause")

# # Hide the turtle
# pen.hideturtle()

# # Keep the drawing window open
# turtle.done()

import curses

def draw_button(window, y, x, label):
    button_width = len(label) + 4  # Add padding for the button
    button_height = 3
    
    # Draw the button border
    window.addstr(y, x, '+' + '-' * (button_width - 2) + '+')
    window.addstr(y + 1, x, '|' + ' ' * (button_width - 2) + '|')
    window.addstr(y + 2, x, '+' + '-' * (button_width - 2) + '+')
    
    # Center the label inside the button
    label_x = x + (button_width - len(label)) // 2
    label_y = y + 1
    window.addstr(label_y, label_x, label)

# Initialize curses
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor

# Clear the screen
stdscr.clear()

# Calculate the window size and button positions
max_y, max_x = stdscr.getmaxyx()
button_width = max_x // 3
button_space = (max_x - 3 * button_width) // 2
start_x = button_space
stop_x = button_space + button_width + button_space
pause_x = stop_x + button_width + button_space

# Draw the buttons
draw_button(stdscr, 2, start_x, "Start")
draw_button(stdscr, 2, stop_x, "Stop")
draw_button(stdscr, 2, pause_x, "Pause")

# Refresh the screen
stdscr.refresh()

# Wait for user input
stdscr.getch()

# Clean up curses
curses.endwin()
