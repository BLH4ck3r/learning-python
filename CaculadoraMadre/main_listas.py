from Utilidades.utilidades import limpiar_pantalla, pedir_entero
from Utilidades.listas import menu_listas, validad_lista
from Clases.listas import Listas

def main_listas():
    lista1 = Listas([])
    while True:
        limpiar_pantalla()
        menu_listas()
        opcion2 = pedir_entero("Elija una opción: ")

        if opcion2 == 1:
            ingresada = lista1.pedir_lista()
            print(f"\nLista ingresada: {ingresada}")
            input("Presione ENTER para continuar")

        elif opcion2 == 2:
            if validad_lista(lista1.lista):
                lista1.invertir()
                print(f"\nIngresada = {lista1.lista} \nInversa = {lista1.mostrar()}")
            input("\nPresiona ENTER para continuar...")
        
        elif opcion2 == 3:
            if validad_lista(lista1.lista):
                es = lista1.palindromo()
                if es:
                    print(f"\n{lista1.lista} si es una lista Palindromo")
                else:
                    print(f"\n{lista1.lista} no es una lista Palindromo")
            input("\nPresione ENTER para continuar...")
        
        elif opcion2 == 4:
            if validad_lista(lista1.lista):
                lista1.duplicados()
                print(f"\nIngresada = {lista1.lista} \nModificada {lista1.mostrar()}")
            input("\nPresione ENTER para continuar...")
        
        elif opcion2 == 5:
            if validad_lista(lista1.lista):
                print(f"\nIngresada = {lista1.lista}")
                lista1.ordenamiento()
                print(f"Ordenada = {lista1.mostrar()}")
            input("\nPresione ENTER para continuar..")

        elif opcion2 == 6:
            if validad_lista(lista1.lista):
                print(f"\nLista actual: {lista1.mostrar()}")
                objetivo = pedir_entero("Digite el numero que desea buscar: ")
                indice = lista1.busqueda(objetivo)
                if indice !=-1:
                    print(f"\nEl numero {objetivo} se encuentra en el indice {indice} de la lista")
                else:
                    print(f"\nEl numero {objetivo} no se encuentra en la lista")
            input("\nPresione ENTER para continuar...")
        
        elif opcion2 == 7:
            print("\nRegresando.")
            break
        else:
            print("\n[!]Opcion Erronea")
            input("Presiona ENTER para continuar...")


if __name__ == '__main__':
    main_listas()
