def diagonal(matrix):
    
    diagonalVar = None

    diagonalVar = [ matrix[i][i] for i in range(len(matrix)) ]

    return diagonalVar

def transpose(matrix):
    
    transposedMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposedMatrix

