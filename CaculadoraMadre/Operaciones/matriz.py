from Utilidades.matriz import validar_operaciones, validar_multiplicacion

def sumar_matriz(matriza, matrizb):
    from Clases.matriz import Matriz
    if validar_operaciones(matriza, matrizb):
        resultado = Matriz(matriza.filas, matrizb.columnas)
        for i in range(matriza.filas):
            for j in range(matriza.columnas):
                resultado.matriz[i][j] = matriza.matriz[i][j] + matrizb.matriz[i][j]
        return resultado

def restar_matriz(matriza, matrizb):
    from Clases.matriz import Matriz
    if validar_operaciones(matriza, matrizb):
        resultado = Matriz(matriza.filas, matrizb.columnas)
        for i in range(matriza.filas):
            for j in range(matriza.columnas):
                resultado.matriz[i][j] = matriza.matriz[i][j] - matrizb.matriz[i][j]
        return resultado

def multiplicar_matriz(matriza, matrizb):
    from Clases.matriz import Matriz
    if validar_multiplicacion(matriza, matrizb):
        resultado = Matriz(matriza.filas, matrizb.columnas)
        for i in range(matriza.filas):
            for j in range(matrizb.columnas):
                suma = 0
                for k in range(matriza.columnas):
                    suma += matriza.matriz[i][k] * matrizb.matriz[k][j]
                resultado.matriz[i][j] = suma
        return resultado
