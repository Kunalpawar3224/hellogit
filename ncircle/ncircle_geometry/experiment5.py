import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Define the vertices of the cube
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

# Define the faces of the cube using the vertex indices
faces = [
    [0, 1, 2, 3],
    [3, 2, 7, 4],
    [4, 7, 6, 5],
    [5, 6, 1, 0],
    [1, 6, 7, 2],
    [5, 0, 3, 4]
]

x = []
y = []
z = []
print("vertices:")
for vertex in vertices:
	print(vertex)
	x.append(vertex[0])
	y.append(vertex[1])
	z.append(vertex[2])
	print(vertices)

tupleList = list(zip(x, y, z))
print(tupleList)

poly3d = [[tupleList[faces[ix][iy]] for iy in range(len(faces[0]))] for ix in range(len(faces))]

for iy in range(len(faces[0])):
	print(iy)
# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Create the Poly3DCollection object for the faces
collection = Poly3DCollection(poly3d, facecolors='w', linewidths=1, alpha=0.5)


# Set the face colors
collection.set_facecolor('r')

# Add the collection to the plot
ax.add_collection3d(collection)

# Set labels for each axis
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.show()
