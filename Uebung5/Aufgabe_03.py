from MainWindow import MainWindow
from Objects2D import *

objectList = []
square1 = Square(0,0,(0,0,0),1)
square2 = Square(1, 1, (1, 1, 1), 2)
objectList.append(square1)
objectList.append(square2)

mainWindow = MainWindow(600, 800, name="TestWindow")
mainWindow.mainloop(objectList)
quit()
