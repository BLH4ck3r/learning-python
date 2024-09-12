from colorama import Fore, Style, init

init(autoreset=True)

def menu_matriz():
    print(Fore.CYAN + Style.RESET_ALL + "\t----------Listas----------")
    print(Fore.LIGHTGREEN_EX + "\t| 1. Agregar             |")
    print(Fore.LIGHTGREEN_EX + "\t| 2. Mostrar             |")
    print(Fore.LIGHTGREEN_EX + "\t| 3. Sumar               |")
    print(Fore.LIGHTGREEN_EX + "\t| 4. Restar              |")
    print(Fore.LIGHTGREEN_EX + "\t| 5. Multiplicar         |")
    print(Fore.LIGHTRED_EX + "\t| 6. Atrás               |")
    print(Fore.CYAN + "\t--------------------------")

def validar_operaciones(matriza, matrizb):
    if matriza.filas != matrizb.filas or matriza.columnas != matrizb.columnas:
        print("[!]No se pueden resolver las matrices ya que tienen dimensiones diferentes")
        return False
    return True

def validar_matriz(matriza, matrizb):
    if matriza is None or matrizb is None:
        print("[!]No se ha ingresado ninguna matriz por favor escoja la opción 1")
        return False
    return True

def validar_multiplicacion(matriza, matrizb):
    if matriza.columnas != matrizb.filas:
        print("\n[!]El numero de columnas de la primera matriz es diferente al numero de columnas de la segunda matriz")
        return False
    return True
