columnWidth = 25

name = "Name"
name = name.center(columnWidth, '_')

ort = "Ort"
ort = ort.center(columnWidth, '_')

land = "Land"
land = land.center(columnWidth, '_')

headerContent = [name, ort, land]
headerLine = "|".join(headerContent)

x = True
table = [headerLine]

while x is True:
    name, ort, land = input("Enter name,city and country: ").split()

    name = name.ljust(columnWidth)
    ort = ort.ljust(columnWidth)
    land = land.ljust(columnWidth)

    rowContent = [name, ort, land]
    row = "|".join(rowContent)
    table.append(row)
    abfrage = input("Enter 'y' or 'Y' for another entry: ")
    if 'y' in abfrage:
        x = True
    else:
        x = False

for entry in table:
    print(entry)