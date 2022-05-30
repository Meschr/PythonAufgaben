import numpy as np


class Star:

    def __init__(self):
        self.__brightness = np.random.randint(0, 2)
        self.__neighbors = [None] * 8
        self.__livingNeigbors

    def printStar(self):
        if self.__brightness < 0:
            print('*', sep='', end='')
        else:
            print(' ', sep='', end='')

    def setNeighbors(self, neighborlist):  # neighborslist is an array with 8 Entrys
        self.__neighbors = neighborlist

    def countlivingneigbors(self):
        self.__livingneighbors = 0
        for entry in self.__neighbors:
            if entry.__brightness == 1:
                self.__livingneighbors += 1

    def liveOrDie(self):
        if self.__livingneighbors == 3 or self.__livingneighbors == 2:
            self.__brightness = 1
        else:
            self.__brightness = 0
