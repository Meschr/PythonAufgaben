import pygame  # to use pygame keyboard and mouse control
from pygame.locals import *  # to use constants from pygame directly
from OpenGL.GL import *  # to use features from OpenGL
import random
import time


class MainWindow:  # Class and constructor for main Window

    def __init__(self, windowHeight=480, windowWidth=640, name="Main Window"):
        pygame.init()  # invoke initial
        self.__windowName = name
        pygame.display.set_caption(name)  # set window title
        self.__windowSize = (windowWidth, windowHeight)  # set size (default VGA)
        self.__videoFlags = OPENGL | DOUBLEBUF  # use OpenGl and double Buffer
        # create window with given size and specified video options
        self.__window = pygame.display.set_mode(self.__windowSize, self.__videoFlags)

    def close(self):
        pygame.quit()  # quit pygame to close window

    def changeBackgroundColor(self):
        R = random.random()
        G = random.random()
        B = random.random()
        alpha = 1
        glClearColor(R, G, B, alpha)  # define background color and alpha of window
        glClear(GL_COLOR_BUFFER_BIT)  # clear OpenGL-Buffer and set background color
        pygame.display.flip()

    def mainloop(self, objectList):
        prev_time = time.time()
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)

        running = True
        while running:
            # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
            for event in pygame.event.get():
                # Beenden bei [ESC] oder [X]
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    print("x:"+str(event.pos[0])+" y:"+str(event.pos[1]))
                elif event.type == timer_event:
                    self.changeBackgroundColor()

            #update windows
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            for object in objectList:
                object.update()
            pygame.display.flip()

            #every path of the if/else should be below 1/targetfps time
            target_fps = 60
            curr_time = time.time()  # so now we have time after processing
            diff = curr_time - prev_time  # frame took this much time to process and render
            delay = max(1.0 / target_fps - diff, 0)  # if we finished early, wait the remaining time to desired fps, else wait 0 ms!
            time.sleep(delay)
            fps = 1.0 / (delay + diff)  # fps is based on total time ("processing" diff time + "wasted" delay time)
            prev_time = curr_time
            pygame.display.set_caption("{0}: {1:.2f}".format(self.__windowName, fps))


def OrthogonalProjection(self, xRange=(-10, 10), yRange=(-10, 10), zRange=(0, 1), frame=0):
    # set initial 2D-perspective for scene
    glMatrixMode(GL_PROJECTION) # switch to projection matrix to change settings
    glLoadIdentity() # reset all prior projection matrices (set all to identity)
    # set scene coordinates for orthogonal projection: left, right, bottom, top, near-, far-clipping
    glOrtho(xRange[0]-frame, xRange[1]+frame, yRange[1]+frame, yRange[0]-frame, zRange[0], zRange[1])
    glMatrixMode(GL_MODELVIEW) # switch back to model matrix to create model objects
    glLoadIdentity() # reset all prior transformation matrices (set all to identity)
