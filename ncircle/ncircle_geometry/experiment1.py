import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

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
                    face.append(vertex_index - 1)  # Adjusting 1-based index to 0-based
                faces.append(face)

    return vertices, faces

def draw_model(vertices, faces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for face in faces:
        x = [vertices[vertex_index][0] for vertex_index in face]
        y = [vertices[vertex_index][1] for vertex_index in face]
        z = [vertices[vertex_index][2] for vertex_index in face]
        ax.add_collection3d(Poly3DCollection(plt.Polygon([list(zip(x, y, z))], closed=True, edgecolor='black')))

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

file_path = 'experiment.obj'
vertices, faces = parse_obj_file(file_path)
draw_model(vertices, faces)
