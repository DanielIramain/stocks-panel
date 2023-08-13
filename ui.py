#import alphaVintageConfig as av
from tkinter import *
from tkinter import ttk, messagebox
from stockPanel import Fundamentos, DatosMercado
from stockPanel import simbolo

##Funciones globales
def mostrar_fundamentos():
    # Obtener la opción seleccionada.
    if combo.get() == 'Fundamentos':
        Fundamentos.obtener_fundamentos()
    elif combo.get() == 'Estado de resultados':
        Fundamentos.obtener_estado_resultados()
    elif combo.get() == 'Balance':
        Fundamentos.obtener_balance()
    elif combo.get() == 'Cash Flow':
        Fundamentos.obtener_clash_flow()
    elif combo.get() == 'Ganancias':
        Fundamentos.obtener_ganancias()

def mostrar_entrada():
    valor = entrada_ticker.get()
    print('valor: ', valor)

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

ttk.Button(frame, text='Enviar', command=DatosMercado.obtener_activos_vigentes).grid(column=1, row=0)
ttk.Button(frame, text='Mostrar', command=mostrar_fundamentos).grid(column=2, row=0)
ttk.Button(frame, text='Mostrar ticker', command=mostrar_entrada).grid(column=2, row=1)
combo.place(x=50, y=50)

root.mainloop()