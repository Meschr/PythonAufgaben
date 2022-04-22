import random

# Funktion um Liste codiert auszugeben
def displayListe2D(liste):
    for i in liste:
        for entry in i:
            print(dictionary[entry])
            
# dictionary um Zahlen codiert darzustellen
dictionary = {0: " ", 1: ".", 2: ",", 3: "!"}

# Hauptliste
liste = []
# Listen die in die Hauptliste eingefügt werden
liste1,liste2 = [],[]

# Abfrage wieviele Einträge in einer der Listen sein soll
eingabe = int(input("Who many numbers do you want in the array?"))
for i in range(eingabe):
    liste1.append(random.randint(0,3))
    liste2.append(random.randint(0,3))

liste.append(liste1)
liste.append(liste2)

# Funktionsaufruf
displayListe2D(liste)

