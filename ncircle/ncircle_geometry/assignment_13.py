#import numpy as np

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
    result = [0, 0, 0]  # Initialize the result matrix as a 3x1 matrix
    
    for i in range(len(matrix1)):
        print('i = ', i)
        for j in range(len(matrix2[0])):
            print('j =', j)
            for k in range(len(matrix2)):
                print("k =", k)
                result[i] += matrix1[i][k] * matrix2[k][j]
    
    return result

# Example matrices
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[1],
           [2],
           [3]]

# Multiply matrices
result = multiply_matrices(matrix1, matrix2)

# Print the result
for row in result:
    print(row)
