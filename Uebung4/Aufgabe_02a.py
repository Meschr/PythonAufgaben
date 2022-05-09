class Complex:
    #todo zusatzaufgabe 2a
    def __init__(self, realPart = 0, imagPart=0, imagChar = 'i'):
        self.real = realPart
        self.imag = imagPart
        if imagChar == 'i' or imagChar == 'j':
            self.imagChar = imagChar
        else:
            print("Unsupported complex Character! Changed it to default.")
            self.imagChar = 'i'

    def __str__(self):
        return "{0:f}{1:+f}{2}".format(self.real,self.imag,self.imagChar)
