from Utilidades.utilidades import pedir_entero
from Operaciones.listas import invertir_lista, palindromo_lista, eliminar_duplicados, busqueda_binaria, ordenar_lista

class Listas:
    def __init__(self, lista):
        self.lista = lista
        self.resultado = []
    
    
    def pedir_lista(self):
        cantidad = pedir_entero("Ingrese la cantidad de items para la lista: ")
        self.lista = []
        for i in range(cantidad):
            numeros = pedir_entero(f"[{i+1}]Digite un numero: ")
            self.lista.append(numeros)
        self.resultado = self.lista.copy()
        return self.lista
    
    def ordenamiento(self):
        self.lista = ordenar_lista(self.lista)
        self.resultado = self.lista
    
    def invertir(self):
        self.resultado = invertir_lista(self.lista)
    
    def palindromo(self):
        self.resultado = palindromo_lista(self.lista)

    def duplicados(self):
        self.resultado = eliminar_duplicados(self.lista)
    
    def busqueda(self, objetivo):
        indice= busqueda_binaria(self.lista, objetivo)
        return indice
    
    def mostrar(self):
        return self.resultado
