##Imports
from tkinter import *
from tkinter import ttk, messagebox
from stockPanel import Fundamentos

##Funciones globales
def capturar_datos():
    global simbolo
    
    simbolo = entrada_ticker.get()
    
    print('valor: ', simbolo)
    
    return simbolo

##Interfaz
root = Tk()
ticker = StringVar()
frame = ttk.Frame(root, padding=100)
combo = ttk.Combobox(state='readonly', 
                     values=['Fundamentos', 
                             'Estado de resultados', 
                             'Balance', 
                             'Cash Flow',
                             'Ganancias'])


frame.grid()
ttk.Label(frame, text='Escriba el ticker').grid(column=0, row=0)

entrada_ticker = ttk.Entry(frame)
entrada_ticker.grid(column=0, row=1)

ttk.Button(frame, text='Enviar', command=Fundamentos.obtener_estado_resultados).grid(column=1, row=0)
ttk.Button(frame, text='Mostrar', command=capturar_datos).grid(column=2, row=0)
ttk.Button(frame, text='Mostrar ticker', command='').grid(column=2, row=1)
combo.place(x=50, y=50)

root.mainloop()