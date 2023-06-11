
import turtle
import json
 
#reference: https://pythonguides.com/python-turtle-triangle/
tur = turtle.Turtle()
 
# added the sides of a triangle
a, b, c = 100, 100, 100

# forward method is used to move the turtle forward by the value of the argument that it takes
tur.forward(a)  

# turn to the left direction by the value of the angle given as an argument
tur.left(120)
tur.forward(b)
 
tur.left(120)
tur.forward(c)

# store the sides in a dictionary
triangle = {
        "a": 50,
        "b": 50,
        "c": 50
    }

# Save the triangle sides to a JSON file
with open("triangle.json", "w") as json_file:
    json.dump(triangle, json_file)

# read the json file
with open("triangle.json", "r") as json_file:
        triangle_points = json.load(json_file)

# Scale the triangle by the 5 units
scaled_points = {
        "a1": [5 * triangle["a"]],
        "b1": [5 * triangle["b"]],
        "c1": [5 * triangle["c"]]
    }

# create another instance to draw a second triangle
tri = turtle.Turtle()

# * is used to unpack the elements of a list or tuple, i.e instead of giving [250] it will give us 250
print(*scaled_points["a1"])
print(scaled_points["a1"])
tri.forward(*scaled_points["a1"])  
tri.left(120)
tri.forward(*scaled_points["b1"])
 
tri.left(120)
tri.forward(*scaled_points["c1"])
 
turtle.done()