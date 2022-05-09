from Aufgabe_01abc import Complex


def ComplexNumberFromInput():
    complexString = input()
    if complexString.__contains__('i') or complexString.__contains__('j'):
        strings = complexString.split()
        #todo finish up 
    else:
        print("Invalid Input")
        return


c1 = Complex(1, -0.5)
c2 = Complex(2.44, 5)

c3 = Complex.add(c1,c2)

c3.disp()

ComplexNumberFromInput()

