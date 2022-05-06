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

    def __init__(self, realPart, imagPart, imagChar = 'i'):
        self.real = realPart
        self.imag = imagPart

        if imagChar == 'i' or imagChar == 'j':
            self.imagChar = imagChar
        else:
            self.imagChar = 'i'
    def disp(self):
        complexString = "{0:f}{1:+f}{2}".format(self.real,self.imag,self.imagChar)
        print(complexString)
        return


def add(number1,number2):
    return Complex(number1.real + number2.real, number1.imag + number2.imag, 'i')

