#import alphaVintageConfig as av
from tkinter import *
from tkinter import ttk, messagebox
from stockPanel import Fundamentos, DatosMercado

##Funciones globales
def mostrar_seleccion():
    # Obtener la opción seleccionada.
    if combo.get() == 'Fundamentos':
        Fundamentos.obtener_fundamentos()

root = Tk()
frame = ttk.Frame(root, padding=100)
combo = ttk.Combobox(state='readonly', 
                     values=['Fundamentos', 
                             'Estado de resultados', 
                             'Balance', 
                             'Cash Flow',
                             'Ganancias'])


frame.grid()
ttk.Label(frame, text='Escriba el ticker').grid(column=0, row=0)
ttk.Button(frame, text='Enviar', command=DatosMercado.obtener_activos_vigentes).grid(column=1, row=0)
ttk.Button(frame, text='Mostrar', command=mostrar_seleccion).grid(column=2, row=0)
combo.place(x=50, y=50)

root.mainloop()