from Utilidades.utilidades import pedir_entero
from Operaciones.basicas import sumar_numeros, restar_numeros, multiplicar_numeros, dividir_numeros, potencia_de_un_numero, raiaz_de_un_numero

class Basicas:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.resultado = None

    @staticmethod
    def pedir_numeros():
        num1 = pedir_entero("\nDigite un numero entero: ")
        num2 = pedir_entero("Digite un numero entero: ")
        return num1, num2
    
    def sumar(self):
        self.resultado = sumar_numeros(self.num1, self.num2)

    def restar(self):
        self.resultado = restar_numeros(self.num1, self.num2)
    
    def multiplicar(self):
        self.resultado = multiplicar_numeros(self.num1, self.num2)
    
    def dividir(self):
        while self.num2 == 0:
            print("[!]No se puede dividir entre 0")
            self.num2 = pedir_entero("Digite un numero diferente de cero: ")
        self.resultado = dividir_numeros(self.num1, self.num2)
    
    def potencia(self):
        self.resultado = potencia_de_un_numero(self.num1, self.num2)
    
    def raiz(self):
        self.resultado = raiaz_de_un_numero(self.num1, self.num2)

    def mostrar(self):
        return self.resultado
    
