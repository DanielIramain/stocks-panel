import requests
from tkinter.filedialog import asksaveasfile 

import pandas as pd
import openpyxl
import openpyxl.utils.dataframe

import view

def elegir_funcion(funcion: str):
    URL = f'https://www.alphavantage.co/query?function={funcion}&symbol={view.simbolo}&apikey={view.API_KEY}'

    return URL

def solicitar_informacion():
    '''
    Extrae la información solicitada a través de la API
    Convertimos de JSON a dataframe y transponemos los datos para presentarlos
    '''
    from view import servicio

    global data
    global df
    
    URL = elegir_funcion(servicio)

    request = requests.get(URL)
    data = request.json()
    df = pd.DataFrame.from_dict([data])
    df = pd.DataFrame.transpose(df)

    presentar_informacion()

def presentar_informacion():
    global reportes_cuatrimestrales
    '''
    Pregunta el tipo de servicio y en funcion a ello presenta la informacion
    La estructura de control esta definida segun el servicio solicitado
    '''
    if view.servicio == 'overview':
        try:
            with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
                df.to_excel(file.name)
        except AttributeError:
            print("The user canceled")
    else:
        '''
        Los datos en la variable data deben ser normalizados en un dataframe
        Normalizamos en un dataframe los datos en formato JSON y luego transponemos
        '''
        df_normalizado = pd.json_normalize(data)
        df_normalizado_transpuesto = pd.DataFrame.transpose(df_normalizado)
        
        '''
        Transponemos el dataframe de los datos normalizados
        Accedemos a las ganancias o reportes cuatrimestrales
        '''
        if view.servicio == 'earnings':
            df_reportes_cuatrimestrales = df_normalizado_transpuesto.loc['quarterlyEarnings']
            reportes_cuatrimestrales = df_reportes_cuatrimestrales.iloc[0]
        else:
            df_reportes_cuatrimestrales = df_normalizado_transpuesto.loc['quarterlyReports']
            reportes_cuatrimestrales = df_reportes_cuatrimestrales.iloc[0]

        guardar_informacion()

def guardar_informacion() -> None:
        '''
        Creamos un workbook
        Seleccionamos la worksheet
        '''
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        '''
        Accedemos a cada reporte cuatrimestral
        Escribimos cada reporte (dataframe) en el worksheet
        ''' 
        for reporte in range(0, len(reportes_cuatrimestrales), 1):
            dic_reporte = reportes_cuatrimestrales[reporte]
            df_dic_reporte = pd.DataFrame([dic_reporte])
            
            '''
            Esta condicion evalua si la hoja de trabajo esta vacia para asignar el header
            de lo contrario inserta los datos
            '''
            if worksheet.max_row == 1:
                rows = openpyxl.utils.dataframe.dataframe_to_rows(df_dic_reporte, index=False, header=True)
            else:
                rows = openpyxl.utils.dataframe.dataframe_to_rows(df_dic_reporte, index=False, header=False)

            #Finalmente agrega cada fila a la worksheet
            for r in rows:
                worksheet.append(r)
        
        with asksaveasfile(mode='w', defaultextension='.xlsx') as file:
            workbook.save(file.name)

        print(df_dic_reporte)
        print(worksheet.max_row)