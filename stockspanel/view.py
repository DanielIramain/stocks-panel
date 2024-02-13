from tkinter import Tk, ttk
from tkinter import BOTTOM, TOP

def obtener_fundamentos():
        ###Se encarga de capturar los datos mostrados a través de GUI para ser usados en los métodos
        ###Luego llama a las funciones que corresponden
        from stockspanel import elegir_funcion, solicitar_informacion
        global simbolo
        global servicio
        global API_KEY
        
        simbolo = entrada_ticker.get()
        servicio = combo.get()
        API_KEY = entrada_api_key.get()
        
        print('simbolo: ', simbolo)
        print('servicio: ', servicio)
        print('API KEY: ', API_KEY)

        elegir_funcion(servicio)
        solicitar_informacion()

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
ttk.Button(frame, text='Mostrar datos', command=obtener_fundamentos).pack(side=BOTTOM)

combo.place(x=90, y=30)

root.mainloop()