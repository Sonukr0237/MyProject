def getMatrix():
    print("Enter the matrix of 3*3 matrix row-wise (9 elements total):")
    matrix = []

    for i in range(3):
        row= list(map(int, input().split()))

        if len(row) != 3:
            print("Please enter 3 input per row")
            return getMatrix()
        matrix.append(row)

    return matrix

def addMatrices(matrix1, matrix2):
    result = []

    for i in range(3):
        row = []
        for j in range(3):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result

def multiplyMatrices(matrix1, matrix2):
    result = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    print("Matrix 1:")
    matrix1 = getMatrix()

    print("Matrix 2:")
    matrix2 = getMatrix()

    print("Matrix 1:")
    printMatrix(matrix1)

    print("Matrix 2:")
    printMatrix(matrix2)

    sumMatrix = addMatrices(matrix1, matrix2)
    productMatrix = multiplyMatrices(matrix1, matrix2)

    print("Sum of the matrices:")
    printMatrix(sumMatrix)

    print("Product of the matrices:")
    printMatrix(productMatrix)


if __name__ == "__main__":
    main()