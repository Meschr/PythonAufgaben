x = input("Zahl eingeben: ")
x = x.replace(" ","")

try:
    komplex = complex(x)
    print("Komplex =", komplex, type(komplex))
except:
    print("Kein Zahlendatenformat eingegeben!")
    exit()

betrag = round(abs(komplex),4)
print("Betrag der komplexen Zahl = ", betrag, type(betrag))
integer = int(betrag)
print("Integer = ", integer, type(integer))
binary = bin(integer)
print("Binär = ", binary, type(binary))
hexa = hex(integer)
print("Hexadezimal = ", hexa, type(hexa))
character = chr(integer)
print("String = ", character, type(character))

