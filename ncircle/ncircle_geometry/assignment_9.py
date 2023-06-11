
import turtle
import json
 
#reference: https://pythonguides.com/python-turtle-triangle/
tur = turtle.Turtle()
 
a, b, c = 100, 100, 100
tur.forward(a)  
tur.left(120)
tur.forward(b)
 
tur.left(120)
tur.forward(c)

triangle = {
        "a": 50,
        "b": 50,
        "c": 50
    }

# Save the triangle points to a JSON file
with open("triangle.json", "w") as json_file:
    json.dump(triangle, json_file)

with open("triangle.json", "r") as json_file:
        triangle_points = json.load(json_file)

# Scale the triangle by the factor
scaled_points = {
        "a1": [5 * triangle["a"]],
        "b1": [5 * triangle["b"]],
        "c1": [5 * triangle["c"]]
    }

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