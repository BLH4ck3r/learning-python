from Utilidades.utilidades import pedir_entero
from Operaciones.general import es_par, es_primo, factorial_numero, fibonacci_numero, porcentaje_numero

class General:
    def __init__(self, num1):
        self.num1 = num1
        self.resultado = None
    @staticmethod
    def pedir_numero():
        num1 = pedir_entero("Digite un numero entero: ")
        return num1
    
    def par(self):
        self.resultado = es_par(self.num1)
    
    def primo(self):
        self.resultado = es_primo(self.num1)
    
    def factorial(self):
        self.resultado = factorial_numero(self.num1)
    
    def fibonacci(self):
        self.resultado = fibonacci_numero(self.num1)

    def porcentaje(self, porcent):
        result = porcentaje_numero(self.num1, porcent)
        self.resultado = result
        return self.resultado

    
    def mostrar(self):
        return self.resultado
