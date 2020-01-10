def matrixElementsSum(matrix):
    sum = 0
    for j in range(0,len(matrix[0])):
        for i in range(0,len(matrix)):
            if matrix[i][j] == 0:
                break
            else:
                sum = sum +matrix[i][j]
    return sum
