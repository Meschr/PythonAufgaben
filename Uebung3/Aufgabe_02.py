import random

def getDictionaryEntry(argument):

    # dictionary um Zahlen codiert darzustellen
    dictionary = {0: " ", 1: ".", 2: ",", 3: "!"}

    # '?' ist default Wert wenn nicht in dictionary vorhanden
    return dictionary.get(argument,"?")



# Funktion um Liste codiert auszugeben
def displayListe2D(liste):
    for i in liste:
        for entry in i:
            print(getDictionaryEntry(entry))


# Hauptliste
liste = []
# Listen die in die Hauptliste eingefügt werden
liste1,liste2 = [],[]

# Abfrage wieviele Einträge in einer der Listen sein soll
eingabe = int(input("Who many numbers do you want in the array?"))
for i in range(eingabe):
    liste1.append(random.randint(0,4))
    liste2.append(random.randint(0,5))

liste.append(liste1)
liste.append(liste2)

# Funktionsaufruf
displayListe2D(liste)

