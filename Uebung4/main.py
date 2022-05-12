import Aufgabe_01abc as Cold
import Aufgabe_02a as Cnew
#
# c1 = Cold.Complex(int(input("Enter real part of number")), int(input("Enter imaginary part of number")))
# c2 = Cold.Complex(int(input("Enter real part of number")), int(input("Enter imaginary part of number")))
#
# c1.disp()
# c2.disp()
# c3 = Cold.Complex.add(c1,c2)
# c3.disp()


c4 = Cnew.Complex(3,3,'j')
c5 = Cnew.Complex(6,6,'j')
c6 = c4+c5
c7 = c4-c5
c8 = c4*c5
c9 = c4/c5

print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
print(c9)