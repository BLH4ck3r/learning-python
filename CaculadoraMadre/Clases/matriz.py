from Utilidades.utilidades import pedir_entero
from Operaciones.matriz import sumar_matriz, restar_matriz, multiplicar_matriz

class Matriz:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[0] * columnas for _ in range(filas)]

    
    def pedir_matriz(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j] = pedir_entero(f"Digite un numero para la posición ({i+1}, {j+1}): ")
    
    def sumar(self, otra_matriz):
        return sumar_matriz(self, otra_matriz)
    
    def restar(self, otra_matriz):
        return restar_matriz(self, otra_matriz)
    
    def multiplicar(self, otra_matriz):
        return multiplicar_matriz(self, otra_matriz)
    

    def mostrar(self):
        for fila in self.matriz:
            print(fila)
