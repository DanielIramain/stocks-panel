##Imports
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.fundamentaldata import FundamentalData
import alphaVintageConfig as av
import matplotlib.pyplot as plt
import pandas as pd

##Variables globales
###mercado = input("Ingrese el mercado que desea (ARG/EEUU): ")
mercado = 'EEUU'
###categoria = input("Ingrese la categoría de servicio que desea: ")
categoria = 'Historicos'
simbolo = input("Ingrese el simbolo a buscar: ")
intervalo = input("Ingrese el intervalo a usar: ")

##Funciones globales
def mostrarTabla(ts, data):
    print(ts)
    print(type(ts))
    print(data)
    print(type(data))

class Fundamentos():
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def ObtenerFundamentos(self):
        FUNCION = 'OVERVIEW'
        url = av.URL = f'https://www.alphavantage.co/query?function={FUNCION}&symbol={simbolo}&apikey={av.API_KEY}'
        r = av.requests.get(url)
        data = r.json()

        print(data)
    
    def ObtenerEstadoResultados(self):
        FUNCION = 'INCOME_STATEMENT'
        url = av.URL = f'https://www.alphavantage.co/query?function={FUNCION}&symbol={simbolo}&apikey={av.API_KEY}'
        r = av.requests.get(url)
        data = r.json()

        print(data)

class SeriesDeTiempo():
    def Intradia(simbolo, intervalo):
        if mercado == 'EEUU' and categoria == 'Historicos':
            ts = TimeSeries(key=av.API_KEY, output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=simbolo, interval=intervalo, outputsize='full')
            mostrarTabla(ts, data)
    def IntradiaExtendido(simbolo, intervalo):
        if mercado == 'EEUU' and categoria == 'Historicos':
            ts = TimeSeries(key=av.API_KEY, output_format='csv')
            data, meta_data = ts.get_intraday_extended(symbol=simbolo, interval=intervalo)
            df = pd.DataFrame(data)
            mostrarTabla(ts, data)
            print(df)
            print(ts)
    def DiarioAjustado(simbolo):
        if mercado == 'EEUU' and categoria == 'Historicos':
            ts = TimeSeries(key=av.API_KEY, output_format='pandas')
            data, meta_data = ts.get_daily_adjusted(simbolo)
            mostrarTabla(ts, data)

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


f = Fundamentos(simbolo)
f.ObtenerEstadoResultados()