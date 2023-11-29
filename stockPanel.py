#Clases
class Fundamentos():
    def __init__(self, simbolo: str):
        self.simbolo = simbolo

        return self

    def obtener_fundamentos():
        from controller import servicio
        from controller import elegir_funcion, solicitar_informacion
        
        elegir_funcion(servicio)
        solicitar_informacion()