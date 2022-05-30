import Star_Class as star


class Universe:

    def __init__(self, row, col):
        self.__row = row
        self.__col = col
        self.__matrix = []

        for r in self.__row:
            for c in self.__col:
                self.__matrix[r][c] = (star.Star())

        for r in self.__row:
            for c in self.__col:
                neighbors = [self.__matrix[r - 1][c - 1], self.__matrix[r - 1][c], self.__matrix[r - 1][(c - 1) % col],
                             self.__matrix[r][c - 1], self.__matrix[r][(c + 1) % col],
                             self.__matrix[(r + 1) % row][c - 1], self.__matrix[(r + 1) % row][c],
                             self.__matrix[(r + 1) % row][(c - 1) % col]]

                self.__matrix[r][c].setNeighbors(neighbors)

    def display(self):
        for r in range(self.__row):
            print()
            for c in range(self.__col):
                self.__matrix[r][c].printStar()
