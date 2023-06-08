import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


def parse_obj_file(file_path):
	''' parser function to read a given 3d ASCCI Obj file
	'''

	vertices = []
	faces = []
	face1 = []
	
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
				face1 = [
                        [0, 1, 2, 3],
                        [3, 2, 7, 4],
                        [4, 7, 6, 5],
                        [5, 6, 1, 0],
                        [1, 6, 7, 2],
                        [5, 0, 3, 4]
                        ]
				print("length =",len(face1))
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
		print(x,y,z)
        
		print("Faces:")
		for face in faces:
			face1.append(face)
			print(face1)
		print(faces)
        



	#reference: https://medium.com/@alexeyyurasov/3d-modeling-with-python-c21296756db2
	# to draw mesh
		fig = plt.figure()
		ax = fig.add_subplot(111, projection = '3d')
		
        
		tupleList = list(zip(x, y, z))
		poly3d = [[tupleList[face1[ix][iy]] for iy in range(len(face1[0]))] for ix in range(len(face1))]
		ax.scatter(x,y,z)
		#ax.scatter(x,y,z ,c = 'r', marker = 'o')
		collection = Poly3DCollection(poly3d, facecolors='w', linewidths=1, alpha=0.5)

		collection.set_facecolor('r')

		ax.add_collection3d(collection)

		plt.show()
	return vertices, faces
parse_obj_file('obj_file.obj')