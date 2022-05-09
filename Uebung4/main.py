import Aufgabe_01abc as Cold
import Aufgabe_02a as Cnew

c1 = Cold.Complex(int(input("Enter real part of number")), int(input("Enter imaginary part of number")))
c2 = Cold.Complex(int(input("Enter real part of number")), int(input("Enter imaginary part of number")))

c1.disp()
c2.disp()
c3 = Cold.Complex.add(c1,c2)
c3.disp()


c4 = Cnew.Complex(5.5,1.2,'j')
print(c4)