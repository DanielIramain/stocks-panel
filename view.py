from tkinter import *
from tkinter import ttk
from tkinter import BOTTOM, TOP

from controller import capturar_datos
from stockPanel import Fundamentos

#GUI
###Ventana principal de la aplicacion
root = Tk()
frame = ttk.Frame(root, padding=100)
combo = ttk.Combobox(root, state='readonly', 
                     values=['overview', 
                             'income_statement', 
                             'balance_sheet', 
                             'cash_flow',
                             'earnings'])


frame.grid()
ttk.Label(frame, text='Escriba un ticker').pack(side='top')

entrada_ticker = ttk.Entry(frame)
entrada_ticker.pack(side=TOP)
ttk.Label(frame, text='Escriba su clave').pack(side='top')
entrada_api_key = ttk.Entry(frame)
entrada_api_key.pack(side=TOP)

ttk.Button(frame, text='Salir', command=quit).pack(side=BOTTOM)
ttk.Button(frame, text='Mostrar datos', command=Fundamentos.obtener_fundamentos).pack(side=BOTTOM)
ttk.Button(frame, text='Guardar datos', command=capturar_datos).pack(side=BOTTOM)
combo.place(x=90, y=30)

root.mainloop()