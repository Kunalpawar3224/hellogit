import numpy as np
from stl import mesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d

def parse_obj_file(file_path):
    vertices = []
    faces = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()

            if parts[0] == 'v':
                vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                vertices.append(vertex)
            elif parts[0] == 'f':
                face = []
                for part in parts[1:]:
                    vertex_index = int(part.split('/')[0])
                    face.append(vertex_index)
                faces.append(face)

    return vertices, faces

vertices, faces = parse_obj_file('experiment.obj')

# Print the vertices
print('Vertices:')
for vertex in vertices:
    print(vertex)

# Print the faces
print('Faces:')
for face in faces:
    print(face)

print(vertices)
print(faces)

#mesh_data = mesh.Mesh.from_file('experiment.obj')
#print(mesh_data)

#reference: https://stackoverflow.com/questions/56559379/plot-mesh-stored-as-vertices-and-faces
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
v = np.array(vertices)
f = np.array(faces) 
C = np.array([1,2,3,4,5,6,7,8,2,3,4,5])
norm = plt.Normalize(C.min(), C.max())
#colors = ['r', 'w', 'g', 'b', 'y', 'm']0
colors = plt.cm.viridis(norm(C))
pc = art3d.Poly3DCollection(v[f], facecolors=colors, edgecolor="black")
ax.add_collection(pc)
plt.show()