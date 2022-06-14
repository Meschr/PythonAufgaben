from Aufgabe_03_1 import Star


class Universe:

    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__matrix = [[0 for x in range(col)] for y in range(row)]

        for r in range(0, self.__row):
            for c in range(0, self.__col):
                self.__matrix[r][c] = Star()

        for r in range(0, self.__row):
            for c in range(0, self.__col):
                neighbors = [self.__matrix[r - 1][c - 1], self.__matrix[r - 1][c], self.__matrix[r - 1][(c - 1) % col],
                             self.__matrix[r][c - 1], self.__matrix[r][(c + 1) % col],
                             self.__matrix[(r + 1) % row][c - 1], self.__matrix[(r + 1) % row][c],
                             self.__matrix[(r + 1) % row][(c - 1) % col]]

                self.__matrix[r][c].setNeighbors(neighbors)

    def display(self):
        for r in range(self.__row):
            print()
            for c in range(self.__col):
                self.__matrix[r][c].display()


    def nextGeneration(self):
        for r in range(0, self.__row):
            for c in range(0, self.__col):
                self.__matrix[r][c].countLivingNeighbors()

        for ro in range(0, self.__row):
            for co in range(0, self.__col):
                self.__matrix[ro][co].liveOrDie()