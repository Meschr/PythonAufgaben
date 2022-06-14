import numpy as np


class Star:

    def __init__(self):
        self.__brightness = np.random.randint(0, 2)
        self.__neighbors = [None] * 8
        self.__livingNeighbors = 0

    def display(self):
        if self.__brightness == 1:
            print('*', sep='', end='')
        else:
            print(' ', sep='', end='')

    def setNeighbors(self, neighborList):  # neighborslist is an array with 8 Entrys
        self.__neighbors = neighborList

    def countLivingNeighbors(self):
        self.__livingNeighbors = 0
        for entry in self.__neighbors:
            if entry.__brightness == 1:
                self.__livingNeighbors += 1

    def liveOrDie(self):
        if self.__livingNeighbors == 3 or self.__livingNeighbors == 2:
            self.__brightness = 1
        else:
            self.__brightness = 0
