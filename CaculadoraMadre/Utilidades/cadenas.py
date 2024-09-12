from colorama import Fore, Style, init

init(autoreset=True)

def menu_cadenas():
    print(Fore.GREEN + Style.DIM + "\t-----------Cadenas----------")
    print(Fore.GREEN + "\t| 1. Ingresar cadena       |")
    print(Fore.GREEN + "\t| 2. Contar vocales        |")
    print(Fore.GREEN + "\t| 3. Contar Palabras       |")
    print(Fore.RED + "\t| 4. Atrás                 |")
    print(Fore.GREEN + "\t----------------------------")


def cadena_pedir(mensaje):
    while True:
        try:
            cadena = input(mensaje)
            if all(char.isalpha() or char.isspace() for char in cadena):
                return cadena
        except ValueError:
            print("[!]Solo se aceptan letras.")
        

def validar_cadena(cadenas):
    if cadenas is None:
        print("[!]No se ha ingresado ninguna cadena, escoja la opción 1")
        return False
    return True
