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
print(matrix)


