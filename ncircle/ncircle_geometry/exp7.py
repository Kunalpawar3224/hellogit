import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the shape
vertices = [
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [1, -1, 1],
    [-1, 1, 1],
    [-1, 1, -1],
    [-1, -1, -1],
    [-1, -1, 1]
]

# Define the faces of the shape using the vertex indices
faces = [
    [0, 1, 2, 3],
    [3, 2, 7, 4],
    [4, 7, 6, 5],
    [5, 6, 1, 0],
    [1, 6, 7, 2],
    [5, 0, 3, 4]
]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vertices as scatter points
x, y, z = zip(*vertices)
ax.scatter(x, y, z, c='r', marker='o')

# Create the Poly3DCollection object for the faces
collection = Poly3DCollection([vertices[face] for face in faces], alpha=0.25)

# Set the face colors
collection.set_facecolor('b')

# Add the collection to the plot
ax.add_collection3d(collection)

# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
