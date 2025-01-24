import tkinter as tk

root = tk.Tk()
root.title("Hier steht der Titel")
root.geometry("400x400")
root.minsize(width=250, height=250)
root.maxsize(width=400, height=400)
root.resizable(width=False, height=True)

label1 = tk.Label(root, text="Label 1", bg="magenta")
label1.pack(side="top", expand=True, fill="y")

label2 = tk.Label(root, text="Label 2", bg="blue")
label2.pack(side="top", expand=True, fill="both")

root.mainloop()