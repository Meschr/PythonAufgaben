import random
import math
import numpy as np

list = []
eingabe = input("Please enter the size of your NxN matrix: ")
eingabe = int(eingabe)
matrixgroese = eingabe ** 2

i = 0
# build random values between -9 und 9 and put it to list
while i < matrixgroese:
    list.append(random.randint(-9, 9))
    i += 1

# list to array
array = np.array(list)

# array to matrix
matrix = np.reshape(array, (eingabe,eingabe))
print(matrix, type(matrix))

row, col = input("Enter the row and col you want to read [],[]: ").split()
row = int(row)
col = int(col)

if row == 0 or row == eingabe - 1 or col == 0 or col == eingabe - 1:
    print("Your index is at the border of the matrix!")
    print(matrix[[row],[col]])
else:
    print("Your index is not at the boarder of the matrix!")
    print(matrix[[row],[col]])
    neighbor1 = int(matrix[[row - 1],[col]])
    print("neighbor 1:", neighbor1)
    neighbor2 = int(matrix[[row + 1],[col]])
    print('neighbor 2:', neighbor2)
    neighbor3 = int(matrix[[row],[col - 1]])
    print('neighbor 3:', neighbor3)
    neighbor4 = int(matrix[[row],[col + 1]])
    print('neighbor 4:', neighbor4)
    neighbor5 = int(matrix[[row + 1],[col - 1]])
    print('neighbor 5:', neighbor5)
    neighbor6 = int(matrix[[row + 1],[col + 1]])
    print('neighbor 6:', neighbor6)
    neighbor7 = int(matrix[[row - 1],[col - 1]])
    print('neighbor 7:', neighbor7)
    neighbor8 = int(matrix[[row - 1],[col + 1]])
    print('neighbor 8:', neighbor8)

    neighborsum = int(matrix[[(row - 1)],[col]] + matrix[[(row + 1)],[col]] + matrix[[row],[col - 1]] + matrix[[row],[col + 1]] + matrix[[row - 1],[col - 1]] + matrix[[row - 1],[col + 1]] \
                  + matrix[[row + 1],[col - 1]] + matrix[[row + 1],[col + 1]])
    print('sum of neighbors:', neighborsum)
    neighborsum = neighbor1 + neighbor2 + neighbor3 + neighbor4 + neighbor5 + neighbor6 + neighbor7 + neighbor8
    print('sum of neighbors:', neighborsum)

