from tkinter import Tk, ttk

#GUI
class StockPanel:
        def __init__(self, master) -> None:
                self.master = master
                master.title('Stock Panel')

                self.combo = ttk.Combobox(master, state='readonly', 
                     values=['overview', 
                             'income_statement', 
                             'balance_sheet', 
                             'cash_flow',
                             'earnings'])
                self.combo.pack()

                self.label_ticker = ttk.Label(master, text='Escriba un ticker').pack(side='top')
                self.ticker = ttk.Entry(master)
                self.ticker.pack()

                self.label_key = ttk.Label(master, text='Escriba su clave').pack(side='top')
                self.api_key = ttk.Entry(master)
                self.api_key.pack()

                self.close_button = ttk.Button(master, text='Salir', command=master.quit)
                self.close_button.pack()

                self.save_button = ttk.Button(master, text='Guardar datos', command=self.capture_data)
                self.save_button.pack()

        def capture_data(self):
                '''
                Se encarga de capturar los datos mostrados a través de la GUI para ser usados en los métodos
                Luego llama a las funciones que corresponden
                '''
                from stockspanel import choose_service, request_information
                
                global service
                global simbol
                global api_key
                
                service = self.combo.get()
                simbol = self.ticker.get()
                api_key = self.api_key.get()
                
                choose_service(service)
                request_information()