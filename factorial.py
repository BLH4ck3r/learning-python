print(f"\nFactorial de un numero\n")

while True:
  try:
    numero = int(input("Digite un numero entero: "))
    if numero < 0:
      print("[!]Error, solo se aceptan números positivos")
    break
  except ValueError:
    print("[!]Error, solo se aceptan números enteros.")

def factorial(numero):
  if numero < 2:
    return 1
  else:
    return numero * factorial(numero - 1)

print(f"\n{numero} = {factorial(numero)}")
