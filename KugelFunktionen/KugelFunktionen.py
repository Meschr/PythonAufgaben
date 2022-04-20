import math
def schnittRadius(radius = 1, winkel = 90):
    a = radius*math.sin(math.radians(abs(winkel)%180))
    return a

def schnittHoehe(radius = 1, winkel = 90):
    h = radius*(1-math.cos(math.radians(abs(winkel%180))))
    return h

def schnittFlaeche(radius = 1, winkel = 90):
    a = schnittRadius(radius, winkel)
    return math.pi * pow(a, 2)

def teilVolumen(radius = 1, winkel = 90):
    h = schnittHoehe(radius, winkel)
    return math.pi/3*math.pow(h, 2)*(3*radius-h)

print(schnittRadius())
print(schnittFlaeche())
print(schnittHoehe())