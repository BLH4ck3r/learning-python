from Utilidades.utilidades import pedir_entero, limpiar_pantalla
from Utilidades.basicas import menu_basicas
from Clases.basicas import Basicas

def main_basicas():
    
    while True:
        limpiar_pantalla()
        menu_basicas()
        opcion1 = pedir_entero("Escoja una opción: ")
        if opcion1 == 1:
            num1, num2 = Basicas.pedir_numeros()
            resultado = Basicas(num1, num2)
            resultado.sumar()
            print(f"\n{num1} + {num2} = {resultado.mostrar()}")
            input("Presione ENTER para continuar...")

        elif opcion1 == 2:
            num1, num2 = Basicas.pedir_numeros()
            resultado = Basicas(num1, num2)
            resultado.restar()
            print(f"\n{num1} - {num2} = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")

        elif opcion1 == 3:
            num1, num2 = Basicas.pedir_numeros()
            resultado = Basicas(num1, num2)
            resultado.multiplicar()
            print(f"\n{num1} x {num2} = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")

        elif opcion1 == 4:
            num1, num2 = Basicas.pedir_numeros()
            resultado = Basicas(num1, num2)
            resultado.dividir()
            num2 = resultado.num2
            print(f"\n{num1} / {num2} = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")
        
        elif opcion1 == 5:
            num1 = pedir_entero("Digite un numero: ")
            num2 = pedir_entero("¿Con qué cantidad desea realizar la potencia?: ")
            resultado = Basicas(num1, num2)
            resultado.potencia()
            print(f"\n{num1}^({num2}) = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")
        
        elif opcion1 == 6:
            num1 = pedir_entero("Digite un numero: ")
            num2 = pedir_entero("Digite el numero de la raiz: ")
            resultado = Basicas(num1, num2)
            resultado.raiz()
            print(f"\n{num1} = {resultado.mostrar()}")
            input("\nPresione ENTER para continuar...")

        elif opcion1 == 7:
            print("Regresando...")
            break
        else:
            print("[!]Opción Erronea.. ")
    
if __name__ == '__main__':
    main_basicas()
