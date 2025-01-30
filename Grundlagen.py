# Python

# Grundlagen

# Ganzzahlen (Integer)
x = 10

# Kommazahlen (Float)
pi = 3.14

# Zeichenkette (String)
name = "Pascal"

# Boolesche Werte (Boolean)
is_wahr = True
is_falsch = False

# Listen
zahl_liste = [1, 2, 3, 4, 5]

# Erstelle eine Variable mein_name mit deinem Namen und gib sie mit print() aus.
mein_name = "Pascal"
print(mein_name)

# Definiere eine Liste mit deinen drei Lieblingszahlen und gib die zweite Zahl aus.
lieblingszahl = [1,1312,3]

print(lieblingszahl[1])

# Bedingungen und Schleifen
#  Bedingungen (if-elif-else)
x = 10
if x > 5:
    print("x ist größer als 5")
elif x == 5:
    print("x ist genau 5")
else:
    print("x ist kleiner als 5")

# Schleifen
#  For-Schleife
for zahl in range(1, 6):
    print(zahl)

# While-Schleife
counter = 0
while counter < 3:
    print("Zähler", counter)
    counter += 1

# Funktionen
def begruessung(name):
    return f"Hallo, {name}!"
print(begruessung("Bob"))

def quadrat(laenge):
    return f"Quadrat: {laenge * laenge}"
print(quadrat(3))

# Benutzerinteraktionen

name = input("Wie heißt du?")
print(f"Hallo, {name}!")

deineZahl = int(input("Wie ist deine Lieblingszahl?"))
print(f"Das Ergebniss ist: {deineZahl * deineZahl}")



