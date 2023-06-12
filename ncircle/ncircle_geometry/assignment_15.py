import numpy as np

def parse_stl(filename):
    vertices = []
    faces = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            tokens = line.strip().split()

            if len(tokens) > 0:
                if tokens[0] == 'vertex':
                    vertex = [float(tokens[1]), float(tokens[2]), float(tokens[3])]
                    vertices.append(vertex)

                elif tokens[0] == 'facet':
                    face = [int(tokens[2]) - 1, int(tokens[5]) - 1, int(tokens[8]) - 1]
                    faces.append(face)

    return np.array(vertices), np.array(faces)


def convert_to_indexed(vertices, faces):
    indexed_vertices = []
    indexed_faces = []

    vertex_index_map = {}
    index = 0

    for face in faces:
        indexed_face = []

        for vertex in face:
            key = tuple(vertices[vertex])

            if key not in vertex_index_map:
                vertex_index_map[key] = index
                indexed_vertices.append(vertices[vertex])
                index += 1

            indexed_face.append(vertex_index_map[key])

        indexed_faces.append(indexed_face)

    return np.array(indexed_vertices), np.array(indexed_faces)


filename = 'stl_file.stl'  # Replace with your STL file
vertices, faces = parse_stl(filename)
indexed_vertices, indexed_faces = convert_to_indexed(vertices, faces)

print('Indexed Vertices:')
print(indexed_vertices)
print('Indexed Faces:')
print(indexed_faces)
