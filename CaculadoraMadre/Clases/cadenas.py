from Utilidades.cadenas import cadena_pedir
from Operaciones.cadenas import contar_vocales, contar_palabras


class Cadenas:
    def __init__(self, cadena):
        self.cadena = cadena
        self.resultado = cadena

    @staticmethod
    def pedir_cadena():
        cadena = cadena_pedir("\nDigite una cadena de texto: ")
        return cadena
    
    def vocales(self):
        self.resultado = contar_vocales(self.cadena)
    
    def palabras(self):
        self.resultado = contar_palabras(self.cadena)
    
    def mostar(self):
        return self.resultado
