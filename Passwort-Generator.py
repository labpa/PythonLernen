import random
import string

def passwort_generator(laenge):
    zeichen = string.ascii_letters + string.digits + string.punctuation
    passwort = ''.join(random.choice(zeichen) for _ in range(laenge))
    return passwort

# Benutzer-Eingabe
try:
    laenge = int(input("Gib die gewünschte Passwortlänge ein: "))
    print("Dein sicheres Passwort: ", passwort_generator(laenge))
except ValueError:
    print("Bitte eine gültige Zahl eingeben!")