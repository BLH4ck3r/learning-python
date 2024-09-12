from colorama import Fore, Style, init

init(autoreset=True)

def menu_basicas():
    print(Fore.CYAN + Style.BRIGHT + "\t--------Basicas--------")
    print(Fore.YELLOW + "\t| 1. Suma             |")
    print(Fore.YELLOW + "\t| 2. Resta            |")
    print(Fore.YELLOW + "\t| 3. Multiplicación   |")
    print(Fore.YELLOW + "\t| 4. División         |")
    print(Fore.YELLOW + "\t| 5. Potencia         |")
    print(Fore.YELLOW + "\t| 6. Raiz             |")
    print(Fore.RED + "\t| 7. Atrás            |")
    print(Fore.CYAN + "\t-----------------------")

