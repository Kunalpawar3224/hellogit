import turtle

# create screen
# root = turtle.Screen()
# canvas = root.getcanvas()
# s = turtle.TurtleScreen(canvas)


# create turtle
t = turtle.Turtle()

# pick the pen up
t.up() 
t.goto(-300, 0)
# pick the pen down
t.down() 

#first half distance of first side of square
t.forward(50)
#cicle having radius 50
t.circle(50)
#other half distance of first side
t.forward(50)

# draw the square
for i in range(3):
	t.left(90)
	t.forward(100)

t.up() 
t.goto(-250, 40)
t.down() 
t.write("Start", align="center", font=("Arial", 14, "bold"))

	
t.up() 
t.goto(-100, 0)
t.down() 

#first half distance of first side of square
t.left(90)
t.forward(50)
#cicle having radius 50
t.circle(50)
#other half distance of first side
t.forward(50)

# draw the square
for i in range(3):
	t.left(90)
	t.forward(100)
	
t.up() 
t.goto(-50, 40)
t.down() 
t.write("Stop", align="center", font=("Arial", 14, "bold"))

	
t.up() 
t.goto(100, 0)
t.down() 

#first half distance of first side of square
t.left(90)
t.forward(50)
#cicle having radius 50
t.circle(50)
#other half distance of first side
t.forward(50)

# draw the square
for i in range(3):
	t.left(90)
	t.forward(100)
    
t.up() 
t.goto(150, 40)
t.down() 
t.write("Pause", align="center", font=("Arial", 14, "bold"))

# delete the Screen when done
turtle.done()