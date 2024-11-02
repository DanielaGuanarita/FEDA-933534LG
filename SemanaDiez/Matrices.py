#Las matrices son una lista de listas, conoce como una estructura bidimencional

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][0], matrix[1][1], matrix[2][2])
# print(matrix)


matrix[1][1] = 'Gato'

def print_matrix(matrix):
    for row in matrix:   # --- > recorre las filas
        for element in row:     # -----> recorre columnas
            print(element, end=' | ')
        print("\n") 


matrix_1 = [[1,2], [3,4]]
matrix_2 = [[5,6], [7,8]]

#suma = [[6,8], [10,12]]

suma = [[0,0], [0,0]]

for i in range(len(matrix_1)):
    for j in range((len(matrix_2))):
        suma[i][j] = matrix_1[i][j] + matrix_2[i][j]
        
print_matrix(suma)
