# PythonLernen
Um Python zu lernen, soll hier eine Sammlung der Grundlagen entstehen.
Ziel ist es am Ende die Zertifizierungen *PCEP* und *PCAP* erfolgreich abzuschließen.

## Grundlagen.py
Übersicht unterschiedlicher Datentypen, schleifen, funktionen und Benutzerinteraktionen

## Gui.py
Erste versuche mit tkinter (Tk interface) GUI Toolkit für Python

### Tkinter Variablen
+ tk.IntVar()
+ tk.DoubleVar()
+ tk.StringVar()
+ tk.BooleanVar()

```python
text_variable = tk.BooleanVar()
text_variable.set(True)

label1 = ttk.Label(root, textvariable=text_variable)
label1.pack()

text_variable.set(False)
print(text_variable.get())
```
### Button Widget
+ Erzeugen eines Button
```Python
button1 = ttk.Button(root, text="Klick mich!")
button1.pack()
 ```
+ Anzeigen aller Möglichkeiten die der Button bietet
```Python
for item in button1.keys():
    print(item, ":", button1[item])
```
+ Zuweisung einer Funktion
  + Das Schlüsselwort zum Ausführen der Funktion bei einem Klick ist command
```Python
# Funktion die in der Console einen Text ausgibt.
def say_hello():
    print("Hallo, danke fürs klicken!")

# Aufrufen der Funktion über Klicken -> command=say_hello
button1 = ttk.Button(root, text="Klick mich!", padding=10, command=say_hello)
button1.pack()
```

### Entry Widget

### Zusätzliche Installation
+ Füge das Paket pillow hinzu um Bilder ausgeben zu können

### Unterschiede
+ tk Widgets
+ ttk Widgets 
  + Moderner 

### Zwischenstand Objekte mit Bildern werden erzeugt.
```python
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Hier steht der Titel")
root.geometry("400x400")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
root.resizable(width=False, height=True)

# Ändern des Themes um aktuelle Änderungen überhaupt anwenden zu können -> Wäre hier nicht nötig gewesen.
style= ttk.Style()
style.theme_use("clam")

# Erzeuge eines Objektes mit Inhalt des Logos
image = Image.open("labpa.jpg").resize((150,150))
photo = ImageTk.PhotoImage(image)

label1 = ttk.Label(root,text="Das ist mein Logo", image=photo, compound="top", padding="50")
label1.pack()

label1.configure(background="red",font=("Courier", 20))

print(label1.keys())

# Ausgabe aller Möglichkeiten in der Console.
for item in label1.keys():
    print(item, ": ", label1[item])

root.mainloop()
```


## Passwort-Generator.py
Als erstes kleines Programm wurde ein Passwort Generator erstellt.
Die gewünschte Länge des Passworts wird in der Konsole angefragt. Nach eingabe einer Zahl (Integer) wird das generierte Passwort im Terminal ausgegeben.

TODO:  
+ Der Passwort-Generator soll mit Tkinter eine grafische Oberfläche bekommen
+ Das erzeugte Passwort soll in Zukunft bei Bedarf gespeichert werden.

## Playground.py
Platz um Ideen auszutesten.
