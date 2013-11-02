import random
import math

random.seed()  # Zufallsgenerator initialisieren

for i in range(10):
    wuerfel = random.randint(1, 6)  # Zufallszahl zwischen 1 und 6 erzeugen
    print("Du hast eine ", wuerfel, " gewuefelt")

print("")  # Zeilenumbruch
print("Die Wurzel aus 254 ist: ", math.sqrt(254))