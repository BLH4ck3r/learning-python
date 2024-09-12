from Utilidades.utilidades import limpiar_pantalla, pedir_entero
from Utilidades.general import menu_generales
from Clases.general import General

def main_general():
    
    while True:
        limpiar_pantalla()
        menu_generales()
        opcion3 = pedir_entero("Escoja una opción: ")
        if opcion3 == 1:
            numero = General.pedir_numero()
            resultado = General(numero)
            resultado.par()
            if resultado.mostrar():
                print(f"\n{numero} es par")
            else:
                print(f"\n{numero} es impar")
            input("\nPresione ENTER para continuar...")
        
        elif opcion3 == 2:
            numero = General.pedir_numero()
            resultado = General(numero)
            resultado.primo()
            if resultado.mostrar():
                print(f"\n{numero} es primo")
            else: 
                print(f"\n{numero} no es primo")
            input("\nPresione ENTER para continuar...")
        
        elif opcion3 == 3:
            numero = General.pedir_numero()
            resultado = General(numero)
            resultado.factorial()
            print(f"\nFactorial \n{numero} = {resultado.mostrar()}")
            input("\Presione ENTER para continuar...")
        
        elif opcion3 == 4:
            numero = General.pedir_numero()
            resultado = General(numero)
            resultado.fibonacci()
            print(f"\nFibonacci \n{numero} = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")
        
        elif opcion3 == 5:
            numero = General.pedir_numero()
            porcent = pedir_entero("Digite el porcentaje que desear calcular: ")
            resultado = General(numero)
            resultado.porcentaje(porcent)
            print(f"\n El {porcent}% de {numero} = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")
        
        elif opcion3 == 6:
            print("\nRegresando.")
            break
        else:
            print("\n[!]Opción Erronea")
            input("Presione ENTER para continuar...")
    
if __name__ == '__main__':
    main_general()
