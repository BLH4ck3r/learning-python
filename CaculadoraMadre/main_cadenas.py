from Utilidades.utilidades import pedir_entero, limpiar_pantalla
from Utilidades.cadenas import menu_cadenas, validar_cadena
from Clases.cadenas import Cadenas

def main_cadenas():

    resultado = None
    while True:
        limpiar_pantalla()
        menu_cadenas()
        opcion4 = pedir_entero("Escoja una opción: ")

        if opcion4 == 1:
            cadena_texto = Cadenas.pedir_cadena()
            resultado = Cadenas(cadena_texto)
            input("\nPresione ENTER para ontinuar...")
        
        elif opcion4 == 2:
            if validar_cadena(resultado):
                resultado.vocales()
                print(f"\n{cadena_texto} tiene {resultado.mostar()} vocales")
            input("\nPresione ENTER para continuar...")
        
        elif opcion4 == 3:
            if validar_cadena(resultado):
                resultado.palabras()
                print(f"\n{cadena_texto} tiene {resultado.mostar()} palabras")
            input("\nPresione ENTER para continuar...")
        
        elif opcion4 == 4:
            print("Regresando.")
            break
        else:
            print("[!]Opción Erronea")
            input("Presione ENTER para continuar...")

if __name__ == '__main__':
    main_cadenas()
