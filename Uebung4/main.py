import Aufgabe_01 as C

c1 = C.Complex(int(input("Enter real part of number")), int(input("Enter imaginary part of number")))
c2 = C.Complex(int(input("Enter real part of number")), int(input("Enter imaginary part of number")))

c1.disp()
c2.disp()
c3 = C.add(c1,c2)
c3.disp()