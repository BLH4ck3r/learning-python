from matriz import Matriz
from utilidades import mostrar_menu, validar_matriz, limpiar_pantalla, pedir_entero


def main():

  mi_matriz_a = None
  mi_matriz_b = None

  while True:
    limpiar_pantalla()
    print("\n\tBienvenido al programa de matrices\n")
    mostrar_menu()

    opcion = pedir_entero("Escoja una opción: ")
    if opcion == 1:
      fila_a = pedir_entero("\n\tMatriz A\nDigite el numero de filas: ")
      columna_a = pedir_entero("Digite el numero de columnas: ")
      mi_matriz_a = Matriz(fila_a, columna_a)
      mi_matriz_a.pedir_matriz()

      fila_b = pedir_entero("\n\tMatriz B\nDigite el numero de filas: ")
      columna_b = pedir_entero("Digite el numero de columnas: ")
      mi_matriz_b = Matriz(fila_b, columna_b)
      mi_matriz_b.pedir_matriz()

      input("Presione ENTER para continuar...")

    elif opcion == 2:
      if validar_matriz(mi_matriz_a, mi_matriz_b):
        print("\nMatriz A\n")
        mi_matriz_a.mostrar_matriz()
        print("\nMatriz B\n")
        mi_matriz_b.mostrar_matriz()
      input("Presione ENTER para continuar...")

    elif opcion == 3:
      if validar_matriz(mi_matriz_a, mi_matriz_b):
        resultado = mi_matriz_a.sumar(mi_matriz_b)
        if resultado:
          print("\nMatriz Resultante\n")
          resultado.mostrar_matriz()
      input("Presione ENTER para continuar...")

    elif opcion == 4:
      if validar_matriz(mi_matriz_a, mi_matriz_b):
        resultado = mi_matriz_a.restar(mi_matriz_b)
        if resultado:
          print("\nMatriz Resultante\n")
          resultado.mostrar_matriz()
      input("Presione ENTER para continuar...")

    elif opcion == 5:
      if validar_matriz(mi_matriz_a, mi_matriz_b):
        resultado = mi_matriz_a.multiplicar(mi_matriz_b)
        if resultado:
          print("\nMatriz Resultante\n")
          resultado.mostrar_matriz()
      input("Presione ENTER para continuar...")

    elif opcion == 6:
      print("¡Hasta Luego!")
      break
    else:
      print("[!]Opción Invalida.")


if __name__ == '__main__':
  main()
