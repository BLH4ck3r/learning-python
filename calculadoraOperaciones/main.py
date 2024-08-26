# main.py
from calculos import Calculadora #importamos la clase Calculadora 
import os #importamos libreria os

mi_calculadora = Calculadora() #asignamos la clase Calculadora a la variable mi_calculadora

while True:
    os.system("clear")#limpiamos pantalla
    print(f"\n--------Calculadora--------\n")#imprimimos el menú
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) División")
    print("5) Salir")
    print("---------------------------")

    try:#estructura de control
        opcion = int(input("Digite un opción: "))
        if opcion < 1 or opcion > 5:#rango de opciones
            continue#continua hasta q se digite una opción correcta
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        continue
    if opcion == 5:
        print("Saliendo...")
        break#sale del ciclo
    while True:#ciclo 
        try:
            num1 = float(input("Digite el primer numero: "))
            num2 = float(input("Digite el segundo numero:"))
            break
        except ValueError:
            print("[!]Error, solo se aceptan numeros enteros.")

    if opcion == 1:
        print(mi_calculadora.suma(num1, num2))#llama a la funcion suma de la clase Calculadora
        break
    elif opcion == 2:
        print(mi_calculadora.resta(num1, num2))#llama a la funcion resta de la clase Calculadora
        break#termina el ciclo
    elif opcion == 3:
        print(mi_calculadora.multiplicacion(num1, num2))#llama a la funcion multiplicación de la clase Calculadora
        break
    elif opcion == 4:
        print(mi_calculadora.division(num1, num2))#llama a la funcion división de la clase Calculadora
        break

