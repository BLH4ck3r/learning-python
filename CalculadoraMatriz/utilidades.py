import os

def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("[!]Solo se aceptan numeros enteros.")


def pedir_entero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("[!]Solo se aceptan numeros positivos.")
                continue
            return numero
        except ValueError:
            print("[!]Solo se aceptan numeros enteros.")


def validar_matriz(matriz1, matriz2):
    if matriz1 is None or matriz2 is None:
        print(
            "[!]No hay ingresado ninguna matriz, por favor seleccione la opción 1"
        )
        return False
    return True


def validar_operaciones(matriz1, matriz2):
    if matriz1.filas != matriz2.filas or matriz1.columnas != matriz2.columnas:
        print(
            "[!]Las matrices tienen diferentes dimensiones por lo que no se podrá resolver las matrices."
        )
        return False
    return True


def mostrar_menu():
    print("-------------Menú-------------")
    print("| 1. Ingresar Matriz         |")
    print("| 2. Mostrar Matriz          |")
    print("| 3. Sumar Matriz            |")
    print("| 4. restar Matriz           |")
    print("| 5. Multiplicar Matriz      |")
    print("| 6. Salir                   |")
    print("------------------------------")


def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
