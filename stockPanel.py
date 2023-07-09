##Imports
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import alphaVintageConfig as av
import matplotlib.pyplot as plt
import pandas as pd
import csv

##Variables globales
###mercado = input("Ingrese el mercado que desea (ARG/EEUU): ")
mercado = 'EEUU'
###categoria = input("Ingrese la categoría de servicio que desea: ")
categoria = 'Historicos'
simbolo = input("Ingrese el simbolo a buscar: ")
intervalo = input("Ingrese el intervalo a usar: ")

##Funciones globales
def mostrar_tabla(ts, data):
    print(ts)
    print(type(ts))
    print(data)
    print(type(data))

def elegir_funcion(funcion: str):
    global funcion_elegida
    global URL
    funcion_elegida = funcion
    URL = f'https://www.alphavantage.co/query?function={funcion_elegida}&symbol={simbolo}&apikey={av.API_KEY}'     

    return funcion_elegida, URL

def solicitar_informacion():
    r = av.requests.get(URL)
    data = r.json()

    print(data)

def obtener_listado(funcion:str):
    global funcion_elegida
    global CSV_URL
    
    funcion_elegida = funcion
    CSV_URL = f'https://www.alphavantage.co/query?function={funcion}&apikey={av.API_KEY}'

    with av.requests.Session() as s:
        descarga = s.get(CSV_URL)
        decodificacion = descarga.content.decode('utf-8')
        cr = csv.reader(decodificacion.splitlines(), delimiter=',')
        listado = list(cr)
        ###Si quiero recorrer cada fila e imprimir como una lista cada elemento
        #for fila in listado:
            #print(fila)
        data = pd.DataFrame(listado)
        print(data)

class Fundamentos():
    def __init__(self, simbolo):
        self.simbolo = simbolo

        return self

    def obtener_fundamentos():
        elegir_funcion('OVERVIEW')
        solicitar_informacion()
    
    def obtener_estado_resultados(self):
        elegir_funcion('INCOME_STATEMENT')
        solicitar_informacion()
    
    def obtener_balance(self):
        elegir_funcion('BALANCE_SHEET')
        solicitar_informacion()
    
    def obtener_clash_flow(self):
        elegir_funcion('CASH_FLOW')
        solicitar_informacion()
    
    def obtener_ganancias(self):
        elegir_funcion('EARNINGS')
        solicitar_informacion()

class DatosMercado():
    def __init__(self) -> None:
        return self
    
    def obtener_activos_vigentes():
        ###Obtener listado de activos en vigencia (imprime por pantalla un dataframe)
        obtener_listado('LISTING_STATUS')
    
    def obtener_calendario_ganancias(self):
        ###Obtener listado de companias que presentan ganancias en los proximos meses (3, 6 u 12) 
        CSV_URL = f'https://www.alphavantage.co/query?function=EARNINGS_CALENDAR&horizon=3month&apikey={av.API_KEY}'

        obtener_listado('EARNINGS_CALENDAR')
    
    def obtener_calendario_ipo(self):
        ###Obtener calendario de primera oferta publica en la bolsa (de EEUU)
        obtener_listado('IPO_CALENDAR')

class SeriesDeTiempo():
    def Intradia(simbolo, intervalo):
        if mercado == 'EEUU' and categoria == 'Historicos':
            ts = TimeSeries(key=av.API_KEY, output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=simbolo, interval=intervalo, outputsize='full')
            mostrar_tabla(ts, data)
    def IntradiaExtendido(simbolo, intervalo):
        if mercado == 'EEUU' and categoria == 'Historicos':
            ts = TimeSeries(key=av.API_KEY, output_format='csv')
            data, meta_data = ts.get_intraday_extended(symbol=simbolo, interval=intervalo)
            df = pd.DataFrame(data)
            mostrar_tabla(ts, data)
            print(df)
            print(ts)
    def DiarioAjustado(simbolo):
        if mercado == 'EEUU' and categoria == 'Historicos':
            ts = TimeSeries(key=av.API_KEY, output_format='pandas')
            data, meta_data = ts.get_daily_adjusted(simbolo)
            mostrar_tabla(ts, data)

    #DiarioAjustado(simbolo)

class NoticiasAlpha():
    ###Buscar la forma de acceder a la información del JSON (diccionario) => documentación Alpha Vantage oficial
    def NoticiasMercado(simbolo):
        FUNCION = 'NEWS_SENTIMENT'
        url = av.URL = f'https://www.alphavantage.co/query?function={FUNCION}&tickers={simbolo}&apikey={av.API_KEY}'
        url_request = av.requests.get(url)
        data = url_request.json()

        print(data)
        print(type(data))

    #NoticiasMercado(simbolo)


    def graficador():
        pass
        #data['4. close'].plot()
        #plt.title(f'Serie de tiempo intradiario de {simbolo} con un intervalo de {intervalo}')
        #plt.show()
    
    graficador()

#f = DatosMercado(simbolo)
#f.obtener_activos_vigentes()