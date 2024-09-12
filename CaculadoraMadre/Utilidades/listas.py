from colorama import Fore, Style, init

init(autoreset=True)

def menu_listas():
    print(Fore.CYAN + Style.RESET_ALL + "\t----------Listas----------")
    print(Fore.LIGHTCYAN_EX + "\t| 1. Agregar             |")
    print(Fore.LIGHTCYAN_EX + "\t| 2. Invertir            |")
    print(Fore.LIGHTCYAN_EX + "\t| 3. Palindromo          |")
    print(Fore.LIGHTCYAN_EX + "\t| 4. Eliminar duplicados |")
    print(Fore.LIGHTCYAN_EX + "\t| 5. Ordenar Lista       |")
    print(Fore.LIGHTCYAN_EX + "\t| 6. Busqueda Binaria    |")
    print(Fore.LIGHTCYAN_EX + "\t| 7. Atrás               |")
    print(Fore.CYAN + "\t--------------------------")


def validad_lista(lista):
    if len(lista) == 0:
        print("[!]No ha ingresado ninguna lista por favor ingrese la opción 1")
        return False
    return True 
