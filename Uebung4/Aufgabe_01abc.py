class Complex:

    def __init__(self, realPart = 0, imagPart=0, imagChar = 'i'):
        self.real = realPart
        self.imag = imagPart
        if imagChar == 'i' or imagChar == 'j':
            self.imagChar = imagChar
        else:
            print("Unsupported complex Character! Changed it to default.")
            self.imagChar = 'i'

    def disp(self):
        complexString = "{0:f}{1:+f}{2}".format(self.real,self.imag,self.imagChar)
        print(complexString)
        return

    def add(complexNumber1, complexNumber2):
        return Complex(complexNumber1.real+complexNumber2.real, complexNumber1.imag+complexNumber2.imag, 'i')