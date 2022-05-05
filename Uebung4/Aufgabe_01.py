class Complex:
    real = 0.0
    imag = 0.0
    imagChar = 'i'

    def __init__(self):
        self.real = 0.0
        self.imag = 0.0

    def __init__(self, realPart, imagPart):
        self.real = realPart
        self.imag = imagPart

    def __init__(self, realPart, imagPart, imagChar):
        self.real = realPart
        self.imag = imagPart

    def disp(self):
        complexString = "{0:f}{1:+f}{2}".format(self.real,self.imag,self.imagChar)
        print(complexString)
        return