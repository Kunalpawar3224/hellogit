import numpy as np
from stl import mesh
#reference: https://programming-surgeon.com/en/numpy-stl-2/
stl_data = mesh.Mesh.from_file('stl_file.stl')
print("read the file")
print(stl_data)