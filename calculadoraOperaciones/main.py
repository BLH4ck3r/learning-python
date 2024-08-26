from calculos import Calculadora
import os

mi_calculadora = Calculadora()

while True:
    os.system("clear")
    print(f"\n--------Calculadora--------")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) División")
    print("5) Salir")
    print("---------------------------")

    try:
        opcion = int(input("Digite un opción: "))
        if opcion < 1 or opcion > 5:
            continue
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        continue
    if opcion == 5:
        print("Saliendo...")
        break
    while True:
        try:
            num1 = float(input("Digite el primer numero: "))
            num2 = float(input("Digite el segundo numero:"))
            break
        except ValueError:
            print("[!]Error, solo se aceptan numeros enteros.")

    if opcion == 1:
        print(mi_calculadora.suma(num1, num2))
        break
    elif opcion == 2:
        print(mi_calculadora.resta(num1, num2))
        break
    elif opcion == 3:
        print(mi_calculadora.multiplicacion(num1, num2))
        break
    elif opcion == 4:
        print(mi_calculadora.division(num1, num2))
        break
