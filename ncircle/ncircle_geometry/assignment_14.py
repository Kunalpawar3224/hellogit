import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def parse_obj_file(file_path):
	''' parser function to read a given 3d ASCCI Obj file
	'''

	vertices = []
	faces = []
	
	#will open and read the given object file 
	with open(file_path, 'r') as file:
		#iterate through each lie of the file
		for line in file:
			print(line)

			#remove the extraa spaces in the line
			line = line.strip()
			#if it is not a line it will skip 
			if not line:
				continue
			#splits a string into a list, split where the spaces are availble
			parts = line.split()

			#if parts list's first index begins with v then condition satisfies
			if parts[0] == 'v':
				#took the elements in the list as float from 1st indexd to 3rd index
				vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
				#append the vertex list into the empty list vertices one by one
				vertices.append(vertex)

			#if parts list's first element start with f, then it will satisfies the condition
			elif parts[0] == 'f':
				# declare face as an empty list
				face = []

				#iterate over  parts list and taken the single list element starting from first position i.e index 1 not from 0
				for part in parts [1:]:
					# split the string with , and taken only integer values
					vertex_index = int(part.split('/')[0])

					# append the vertex index values in a list for single face
					face.append(vertex_index)

				#append the multiple face values of list in the single list 
				faces.append(face)

	return vertices, faces



def draw_model(vertices, faces):
	
	# draw the figure
	fig = plt.figure()
	# added the axes fu=ig as 1,1,1
	ax = fig.add_subplot(111, projection = '3d')

	# iterate over the faces, and took single list as face
	for face in faces:
		print(f"The single face is= {face} ")

		# Taken the vertices index i.e if index is 7 then the we take the value of the 6th index vertices.
		# The index-1 is used because the indices in the OBJ file start from 1, while Python lists are zero-based.
		triangle = [vertices[index -1] for index in face]
		print(f"the upper triangle is = {triangle}")
	
		#We have to closed the traingle, hence append the zeroth index of the triangle as a fourth index.
		triangle.append(triangle[0])
		print(f"the lower triangle is = {triangle}")

		# To plot the x,y and z coordinates of the traingle
		# Taken the x coordinates of the single triangle in seperate list 
		x = [vertex[0] for vertex in triangle]
		# Taken the y coordinates of the single triangle in seperate list
		y = [vertex[1] for vertex in triangle]
		# Taken the z coordinates of the single triangle in seperate list
		z = [vertex[2] for vertex in triangle]

		# plotted the above x, y and z coordinates
		ax.plot(x, y, z)
		
	# Give the names to the axes as x, y, z
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_zlabel('z')
	
	# Title of the plotted mesh
	ax.set_title('3d ASCCI Obj')
	
	
	plt.show()


file_path = 'obj_file.obj'

vertices, faces = parse_obj_file(file_path)

draw_model(vertices, faces)