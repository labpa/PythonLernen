import tkinter as tk
from tkinter import ttk

# def print_entry_input():
#     # print(entry1.get())
#     ttk.Label(root, text=entry1.get()).pack()


def delete_input():
    ttk.Label(root, text=entry1.get()).pack()
    entry1.delete(0, tk.END)

root = tk.Tk()
root.title("Hier steht der Titel")
root.geometry("400x400")

entry1 = ttk.Entry(root, width=40)
entry1.pack()



button1 = ttk.Button(root, text="Input Löschen", command=delete_input)
button1.pack()



for item in entry1.keys():
    print(item, ":", entry1[item])



root.mainloop()

