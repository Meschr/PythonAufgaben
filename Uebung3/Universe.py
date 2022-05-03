import numpy as np


def create(rows, *cols):
    if (rows <= 0 & len(cols)>=0):
        matrice = np.random.randint(0, 2, size=(int(cols), int(cols)))

    elif (len(cols)<= 0 & rows >= 0):
        matrice = np.random.randint(0, 2, size=(rows, rows))

    elif (rows <= 0 & len(cols) <= 0):
        matrice = np.random.randint(0, 2, size=(0, 0))

    else:
        matrice = np.random.randint(0, 2, size=(rows, int(cols[0])))

    return matrice


def neighborCount(binaryMatrix, rowPosition, colPosition):
    """Returns the number of Ones in the neighborhood of the given position in the matrix. \n
        First row and column starts with 1 and not with 0!
    """
    neighborCnt = 0

    if rowPosition == 0 or colPosition == 0:
        print("row or column position is 0 (not valid)!")
        return neighborCnt;

    (rows, cols) = binaryMatrix.shape
    for i in range(rowPosition-2, rowPosition+1, 1):
        for j in range(colPosition-2, colPosition+1, 1):
            if i != rowPosition-1 or j != colPosition-1:
                neighborCnt += binaryMatrix[i%rows][j%cols]

    return neighborCnt


def getNeighbors(binaryMatrix):
    neighborMatrix = np.zeros(np.shape(binaryMatrix), dtype=int)

    rows, cols = binaryMatrix.shape

    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            neighborMatrix[i][j] = neighborCount(binaryMatrix,i+1,j+1)

    return neighborMatrix


def display(matrix):
    rows, cols = matrix.shape
    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if matrix[i][j] > 0:
                print('*', end='')
            else:
                print(' ', end='')
        print("")
    return


def nextGeneration(universe, neighbor):
    nextGenUniverese = np.zeros(universe.shape, dtype=int)
    rows, cols = universe.shape

    for i in range(0, rows, 1):
        for j in range(0, cols, 1):
            if neighbor[i][j] == 3 and universe[i][j] == 0:
                nextGenUniverese[i][j] = 1
            elif neighbor[i][j] < 2 and universe[i][j] == 1:
                nextGenUniverese[i][j] = 0
            elif neighbor[i][j] == 2 or 3 and universe[i][j] == 1:
                nextGenUniverese[i][j] = 1
            elif neighbor[i][j] > 3 and universe[i][j] == 1:
                nextGenUniverese[i][j] = 0
    return nextGenUniverese