from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=150)
frm.grid()
ttk.Label(frm, text="Hello world u.u").grid(column=0,row=5)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=0,row=6)
root.mainloop()