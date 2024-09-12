from Utilidades.utilidades import limpiar_pantalla, menu, pedir_entero
from main_basicas import main_basicas
from main_generales import main_general
from main_listas import main_listas
from main_cadenas import main_cadenas
from main_matriz import main_matriz


def main():
    
    while True:
        limpiar_pantalla()
        print("\n\tBienvenido a la Calculadora madre 2.0\n")
        menu()
        opcion = pedir_entero("Digite un numero entero: ")
        if opcion == 1:
            main_basicas()
            input("Presione ENTER para continuar...")
        
        elif opcion == 2:
            main_listas()
            input("Presione ENTER para continuar...")
            
        elif opcion == 3:
            main_general()
            input("Presione ENTER para continuar...")
        
        elif opcion == 4:
            main_cadenas()
            input("Presione ENTER para contonuar...")
        
        elif opcion == 5:
            main_matriz()
            input("\nPresione ENTER para continuar...")

        elif opcion == 6:
            print("¡Hasta Luego!")
            break
        else:
            print("\n[!]Opción Erronea.")
            input("Presione ENTER para continuar...")
            
    
if __name__ == '__main__':
    main()
