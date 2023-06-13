import numpy as np

# Define the 3x3 matrix A
# A = np.array([[1, 2, 3],
#               [4, 5, 6],
#               [7, 8, 9]])

# # Define the 3x1 matrix B
# B = np.array([[1],
#               [2],
#               [3]])

# # Perform the matrix multiplication
# C = np.dot(A, B)

# # Display the result
# print(C)


def multiply_matrices(matrix1, matrix2):
    result = [[0 for x in range(3)] for y in range(3)]  # Initialize the result matrix as a 3x1 matrix
    
    for i in range(len(matrix1)):
        
        for j in range(len(matrix2[0])):
            
            for k in range(len(matrix2)):
            
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example matrices
mat_1 = [[0, 0, 1],
           [0, 1, 0],
           [-1, 0, 0]]

vector_a = [[10, 0, 0]]

# Multiply matrices
transformation_a = multiply_matrices(mat_1, vector_a)

# Print the result
#transformation_a = np.dot(matrix1, matrix2)
print(transformation_a)

matrix_z = [[0.7071, -0.7071, 0], 
            [0.7071 , 0.7071, 0], 
            [0, 0, 1]] 

transformation_z = multiply_matrices(mat_1, matrix_z)
print("transformation_z is =",transformation_z)
transformation_z = np.dot(mat_1, matrix_z)
print("transformation_z is =",transformation_z)

scaling_matrix =[[3, 0, 0], 
                [0 , 3, 0], 
                [0, 0, 3]]

# For rotation around the Y-axis by 45 degrees:
matrix_y = [[0.7071, 0, 0.7071], 
            [0 , 1, 0], 
            [-0.7071, 0, 0.7071]] 

# For rotation around the X-axis by 45 degrees: 
matrix_x = [[1, 0, 0], 
            [0 , 0.7071, -0.7071], 
            [0, 0.7071, 0.7071]] 

if __name__ == "__main__":
    
    transformation_a = multiply_matrices(mat_1, vector_a)
    transformation_z = multiply_matrices(mat_1, matrix_z)
    transformation_scaled_matrix = multiply_matrices(mat_1, scaling_matrix)
    print(transformation_scaled_matrix)
    transformation_around_xy = multiply_matrices(matrix_y, matrix_x)
    print(f"transformation_around_xy = {transformation_around_xy}")
    transformation_a_z = multiply_matrices(transformation_z, vector_a)
    print(f"transformation_a_z = {transformation_a_z}")
    transformation_a_scaled_matrix = multiply_matrices(transformation_scaled_matrix, vector_a)
    print(f"transformation_a_scaled_matrix = {transformation_a_scaled_matrix}")
    transformation_a_xy = multiply_matrices(transformation_around_xy, vector_a)
    print(f"transformation_a_xy = {transformation_a_xy}")

    multiply_matrices(mat_1, vector_a)



