from colorama import Fore, Style, init

init(autoreset=True)

def menu_generales():
    print(Fore.MAGENTA + Style.DIM + "\t-----------General-----------")
    print(Fore.LIGHTBLUE_EX + "\t| 1. Numeros pares          |")
    print(Fore.LIGHTBLUE_EX + "\t| 2. Numeros primos         |")
    print(Fore.LIGHTBLUE_EX + "\t| 3. Factorial de un numero |")
    print(Fore.LIGHTBLUE_EX + "\t| 4. Fibonacci              |")
    print(Fore.LIGHTBLUE_EX + "\t| 5. Porcentajes            |")
    print(Fore.RED + "\t| 6. Atrás                  |")
    print(Fore.MAGENTA + "\t-----------------------------")
