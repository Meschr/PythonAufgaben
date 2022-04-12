tabelle = ['_____Name','Ort','Land_____']
header = "_____|_____".join(tabelle)
tabelle.append(header)
tabelle.remove('_____Name')
tabelle.remove('Ort')
tabelle.remove('Land_____')


x = True
eintrag = []

while x is True:
    name, ort, land = input("Enter name,city and country: ").split()
    eintrag = [name,ort,land]
    eintrag = "\t".join(eintrag)

    tabelle.append(eintrag)

    abfrage = input("Enter 'y' or 'Y' for another entry: ")
    if abfrage == 'y' or 'Y':
        x = False
for entry in tabelle:
    entry.expandtabs(10)
    print(entry+'\n')


print("test")

# i = 1
# for i in range(len(tabelle)):
#
#     if (i % 3) == 0:
#         print(entry)
#         print('\n')
#         i += 1
#     else:
#         print(entry)
#         i += 1