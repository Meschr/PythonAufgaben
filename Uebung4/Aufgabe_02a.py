class Complex:
    # todo zusatzaufgabe

    """
            if str(imagPart).isalpha():
            if str(imagPart) == 'i' or str(imagPart) == 'j':
                imagChar = imagPart
            else:
                print("Unsupported complex Character! Changed it to default.")
                self.imagChar = 'i'
    """

    def __init__(self, realPart=0, imagPart=0, imagChar='i'):
        self.real = realPart
        self.imag = imagPart
        if imagChar == 'i' or imagChar == 'j':
            self.imagChar = imagChar
        else:
            print("Unsupported complex Character! Changed it to default.")
            self.imagChar = 'i'

    def __str__(self):
        return "{0:f}{1:+f}{2}".format(self.real, self.imag, self.imagChar)

    def __add__(self, other):
        return Complex(self.real+other.real, self.imag+other.imag, 'i')

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag, 'i')

    def __truediv__(self, other):
        return Complex(self.real / other.real, self.imag / other.imag, 'i')

    def __mul__(self, other):
        return Complex(self.real * other.real, self.imag * other.imag, 'i')

