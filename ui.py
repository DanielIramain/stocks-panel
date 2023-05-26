#import alphaVintageConfig as av
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Prueba").grid(column=0, row=0)
ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=0)
root.mainloop()