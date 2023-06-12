# Python programme for drawing a square and a rectangle together in # Turtle - Python  
import turtle  
ttl = turtle.Turtle()  
  
#SQUARE  
ttl.up() 
ttl.goto(-100, 0)
ttl.down() 
for j in range(4):  
   ttl.forward(60)  
   ttl.left(90)  
ttl.up()  
ttl.goto(80,0)  
ttl.down()  
  
#RECTANGLE  
  
ttl.forward(120)  
ttl.left(90)  
ttl.forward(80)  
ttl.left(90)  
ttl.forward(120)  
ttl.left(90)  
ttl.forward(80)  
ttl.left(90) 

turtle.done()