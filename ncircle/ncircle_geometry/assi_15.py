import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import assignment_13
import assignment_14

mat_1 = [[0, 0, 1],
           [0, 1, 0],
           [-1, 0, 0]]

scaling_matrix =[[3, 0, 0], 
                [0 , 3, 0], 
                [0, 0, 3]]

var = assignment_13.multiply_matrices(mat_1, scaling_matrix )
print(var)


# Load the 3D model vertex positions into a NumPy array
# vertices = np.array([[0.0, 0.0, 0.0],
#                      [0.0, 0.0, 1.0],
#                      [0.0, 1.0, 0.0],
#                      [0.0, 1.0, 1.0],
#                      [1.0, 0.0, 0.0],
#                      [1.0, 0.0, 1.0],
#                      [1.0, 1.0, 0.0],
#                      [1.0, 1.0, 1.0]])


vertices = assignment_14.vertices
rotated_vertices = []
print(f"vertices is = {vertices}")
for vertex in vertices:
    # Apply the rotation matrix by multiplying it with the vertex
    print(f"vertex is = {vertex}")
    
    rotated_vertex = np.matmul(vertex, var)
    #rotated_vertex = assignment_13.multiply_matrices(var, vertex )
    rotated_vertices.append(rotated_vertex)
    print(f"rotatted vertex is = {rotated_vertex}")

# Now the "rotated_vertices" list contains the transformed vertices
# You can use these vertices to visualize or manipulate the rotated 3D model
print(f"rotatted vertices is = {rotated_vertices}")

faces = assignment_14.faces
assignment_14.draw_model(rotated_vertices, faces)