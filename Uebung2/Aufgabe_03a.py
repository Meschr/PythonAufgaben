eingabe = input("Eingabe hinzufügen: ")

case = eingabe.casefold()               # Ändert Groß- zu Kleinbuchstaben und 'ß' zu 'ss'
low = eingabe.lower()                   # Ändert Groß- zu Kleinbuchstaben
up = eingabe.upper()                    # Ändert Klein- zu Großbuchstaben und 'ß' zu 'SS'
tit = eingabe.title()                   # Macht den ersten Buchstaben des Wortes groß 'ß' zu 'Ss'

print(case, low, up, tit, sep='\n\n')   # sep='\n\n' setzt 2*new Line nach jeder Variablen

komma = eingabe.replace(" ", ",")       # replaced Leerzeichen zu Komma
tab = eingabe.replace(" ", "\t")        # replaced Leerzeichen zu Tab

print(eingabe, komma, tab, sep='\n')

_split =  eingabe.split()               # trennt bei 'c' den String wenn split('c')

_splitlines = eingabe.splitlines()

print(_split,_splitlines, sep= '\n\n')

'''
strip Methode entfernt Character vor und hinter einem String -> sobald ein anderer Character als angegeben im String erscheint 
wird das entfernen gestoppt sobald der letzte "andere" Character durchlaufen wird werden die restlichen entfernt
wenn keine speziellen Character angegben werden werden nur die Leerzeichen entfernt
'''
splitstring = ("..deervsa,,Hallo Welte.,,sdf.el")
print(splitstring.strip('.,dervsalf'))