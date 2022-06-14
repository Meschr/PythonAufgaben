import pygame  # to use pygame keyboard and mouse control
from pygame.locals import *  # to use constants from pygame directly
from OpenGL.GL import *  # to use features from OpenGL
import threading


class MainWindow:  # Class and constructor for main Window

    def __init__(self, windowHeight=480, windowWidth=640, name="Main Window"):
        pygame.init()  # invoke initial settings
        pygame.display.set_caption(name)  # set window title
        self.__windowSize = (windowWidth, windowHeight)  # set size (default VGA)
        self.__videoFlags = OPENGL | DOUBLEBUF  # use OpenGl and double Buffer
        # create window with given size and specified video options
        self.__window = pygame.display.set_mode(self.__windowSize, self.__videoFlags)

    def close(self):
        pygame.quit()  # quit pygame to close window

    def changeBackgroundColor(self):
        threading.Timer(1.0, changeBackgroundColor).start()

        R = random.random()
        G = random.random()
        B = random.random()
        alpha = 1
        glClearColor(R, G, B, alpha)  # define background color and alpha of window
        glClear(GL_COLOR_BUFFER_BIT)  # clear OpenGL-Buffer and set background color

    def mainloop(self):
        changeBackgroundColor()
        while True:
            # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
            for event in pygame.event.get():
                # Beenden bei [ESC] oder [X]
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()

