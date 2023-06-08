class Mesh:
    def __init__(self):
        self.vertices = []
        self.faces = []

    def add_vertex(self, vertex):
        self.vertices.append(vertex)

    def add_face(self, face):
        self.faces.append(face)


def parse_obj_file(file_path):
    mesh = Mesh()

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split()

            if parts[0] == 'v':
                vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
                mesh.add_vertex(vertex)
            elif parts[0] == 'f':
                face = []
                for part in parts[1:]:
                    vertex_index = int(part.split('/')[0])
                    face.append(vertex_index - 1)  # Adjusting 1-based index to 0-based
                mesh.add_face(face)

    return mesh

def draw_model(mesh):
    # Write code to draw the model using the given 3D platform

    file_path = 'experiment.obj'
    mesh = parse_obj_file(file_path)
    draw_model(mesh)
