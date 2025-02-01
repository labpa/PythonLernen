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

