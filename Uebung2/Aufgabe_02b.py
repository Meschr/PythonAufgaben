eingabe = input("Wort eingeben: ")

liste = list(eingabe)               # erstellt Liste mit Charactern der Eingabe
print(liste)

tup = tuple(eingabe)                # erstellt Tuple mit Charactern der Eingabe
print(tup)

sortlist = sorted(liste)            # sortiert nach Alphabet
print(sortlist)

wortliste = eingabe.split()
lensort = sorted(wortliste, key= len)   # sortiert nach Länge der Eingabe
print(lensort)

length = len(liste)                 # zählt die Anzahl der Character
print(length)
x = []
for i in liste:                     # erstellt liste mit Werten der Character
    x.append(ord(i))

_min = min(x)
_max = max(x)

print("Minimum = ", _min)
print("Maximum = ", _max)
print("Ord() Werte: ",x)
_ascii, byte = [], []
for i in tup:
    _ascii.append(ascii(i))
    byte.append(bytes(i,'utf-8'))   # erstellt Liste mit Bytewerten der Character
print(_ascii)
print(byte)