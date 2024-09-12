import os
from colorama import Fore, Style, init

init(autoreset=True)

def menu():
    print(Fore.CYAN + Style.BRIGHT + "\t--------Operaciones--------")
    print(Fore.GREEN + "\t| 1. Basicas              |")
    print(Fore.GREEN + "\t| 2. Listas               |")
    print(Fore.GREEN + "\t| 3. Generales            |")
    print(Fore.GREEN + "\t| 4. Cadenas              |")
    print(Fore.GREEN + "\t| 5. Matriz               |")
    print(Fore.RED + "\t| 6. Salir                |")
    print(Fore.CYAN + "\t---------------------------")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("[!]Solo se aceptan numeros enteros")
            

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')
