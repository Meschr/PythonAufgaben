import KugelFunktionen

# Aufruf der Kugelfunktionen ohne Parameter verwendet die vordefinierten Werte
print("Äquatorfläche Einheitskugel:", KugelFunktionen.schnittFlaeche(),"m²")
print("Gesamtvolumen Einheitskugel:", KugelFunktionen.teilVolumen(),"m³")
winkel = 90
radius= float(input("Bitte Radius in Metern eingeben: "))
while(winkel >= 0):
    print("Schnittfläche bei", winkel,"°:",
    KugelFunktionen.schnittFlaeche(radius, winkel), "m²")
    print("Teilvolumen bei ", winkel,"°:",
    KugelFunktionen.teilVolumen(radius, winkel), "m³")
    print("Teilsegmentoberfläche bei:",winkel,"°",
          KugelFunktionen.oberfläche(radius,winkel),"m²")
    winkel = int(input("Bitte Winkel in ganzen Grad eingeben: "))
