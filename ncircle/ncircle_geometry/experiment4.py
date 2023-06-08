from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

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
    def draw():
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Set up the camera position
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

        glBegin(GL_TRIANGLES)
        for face in mesh.faces:
            for vertex_index in face:
                vertex = mesh.vertices[vertex_index]
                glVertex3fv(vertex)
        glEnd()

        glutSwapBuffers()

    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Model Viewer")
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glutDisplayFunc(draw)
    glutMainLoop()

file_path = 'experiment.obj'
mesh = parse_obj_file(file_path)
draw_model(mesh)
