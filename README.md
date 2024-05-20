# Software de información financiera
Esta aplicación de escritorio facilita la obtención de información financiera de empresas cotizantes en la bolsa de valores de EEUU a través de la API de la compañía Alpha Vantage. 
Los datos son devueltos en formato .xlsx (Excel) para ser posteriormente procesados ya sea por SGBD o plataformas de inteligencia empresarial como Power BI. Actualmente cuenta con **cinco opciones**:
- Overview: información general de la compañía
- Income statement: estados de resultados de los últimos 5 períodos
- Balance sheet: balances de los últimos 5 períodos
- Cash flow: estado financiero donde se muestran los flujos de fondos
- Earnings: datos sobre la fecha de presentación de resultados, ganancias por acción presentadas, EPS esperada y el nivel de "sorpresa" absoluta y relativa.

## Cómo utilizarlo
Se debe reclamar la free API key en [el servicio de Alpha Vantage](https://www.alphavantage.co/support/#api-key). Una vez obtenida, podemos ejecutar el script de Python que abrirá una aplicación de escritorio. Allí nos solicitará los siguientes datos:
1. Servicio a utilizar (información requerida)
2. Ticker
3. API key obtenida
