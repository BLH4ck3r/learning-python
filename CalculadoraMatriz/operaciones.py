from utilidades import validar_operaciones


def sumar_matriz(matriz1, matriz2):
    from matriz import Matriz
    if validar_operaciones(matriz1, matriz2):
        resultado = Matriz(matriz1.filas, matriz2.columnas)
        for i in range(matriz1.filas):
            for j in range(matriz1.columnas):
                resultado.matriz[i][
                    j] = matriz1.matriz[i][j] + matriz2.matriz[i][j]
        return resultado


def restar_matriz(matriz1, matriz2):
    from matriz import Matriz
    if validar_operaciones(matriz1, matriz2):
        resultado = Matriz(matriz1.filas, matriz2.columnas)
        for i in range(matriz1.filas):
            for j in range(matriz1.columnas):
                resultado.matriz[i][
                    j] = matriz1.matriz[i][j] - matriz2.matriz[i][j]
        return resultado


def multiplicar_matriz(matriz1, matriz2):
    from matriz import Matriz
    if matriz1.filas != matriz2.columnas:
        print(
            "[!]No se pueden multiplicar las matrices debido a que el numero columnas es diferentes al numero de filas."
        )
        return None
    else:
        resultado = Matriz(matriz1.filas, matriz2.columnas)
        for i in range(matriz1.filas):
            for j in range(matriz2.columnas):
                suma = 0
                for k in range(matriz1.columnas):
                    suma += matriz1.matriz[i][k] * matriz2.matriz[k][j]
                resultado.matriz[i][j] = suma
        return resultado
