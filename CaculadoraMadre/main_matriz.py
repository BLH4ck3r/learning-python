from Utilidades.utilidades import pedir_entero, limpiar_pantalla
from Utilidades.matriz import menu_matriz, validar_matriz
from Clases.matriz import Matriz

def main_matriz():
    mi_matriz_a = None
    mi_matriz_b = None

    while True:
        limpiar_pantalla()
        menu_matriz()
        opcion5 = pedir_entero("Escoja una opción: ")

        if opcion5 == 1:
            fila_a = pedir_entero("\nMatriz A\nDigite el numero de filas: ")
            columna_a = pedir_entero("Digite el numero de columnas: ")
            mi_matriz_a = Matriz(fila_a, columna_a)
            mi_matriz_a.pedir_matriz()

            fila_b = pedir_entero("\nMatriz B \nDigite el numero de filas: ")
            columna_b = pedir_entero("Digite el numero de columnas: ")
            mi_matriz_b = Matriz(fila_b, columna_b)
            mi_matriz_b.pedir_matriz()
            input("\nPresione ENTER para continuar...")

        elif opcion5 == 2:
            if validar_matriz(mi_matriz_a, mi_matriz_b):
                print("\nMatriz A\n")
                mi_matriz_a.mostrar()
                print("\nMatriz B\n")
                mi_matriz_b.mostrar()
            input("\nPresione ENTER para continuar...")

        elif opcion5 == 3:
            if validar_matriz(mi_matriz_a, mi_matriz_b):
                resultado = mi_matriz_a.sumar(mi_matriz_b)
                if resultado:
                    print("\nMatriz resultante\n")
                    resultado.mostrar()
            input("\nPresione ENTER para continuar...")
        
        elif opcion5 == 4:
            if validar_matriz(mi_matriz_a, mi_matriz_b):
                resultado = mi_matriz_a.restar(mi_matriz_b)
                if resultado:
                    print("\nMatriz Resultante \n")
                    resultado.mostrar()
            input("\nPresione ENTER para continuar...")
        
        elif opcion5 == 5:
            if validar_matriz(mi_matriz_a, mi_matriz_b):
                resultado = mi_matriz_a.multiplicar(mi_matriz_b)
                if resultado:
                    print("\nMatriz Resultante\n")
                    resultado.mostrar()
            input("\nPresione ENTER para continuar...")

        elif opcion5 == 6:
            print("\nRegresando.")
            break
        else:
            print("\n[!]Opción Erronea")
            input("Presione ENTER para continuar...")

if __name__ == '__main__':
    main_matriz()
