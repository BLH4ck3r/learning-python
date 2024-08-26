print(f"\nFibonacci\n")

while True:
  try:
    numero = int(input("Digite un numero entero: "))
    if numero < 0:
      print("[!]Error, solo se aceptan numeros positivos.")
      continue
    break
  except ValueError:
    print("[!]Error, solo se aceptan numeros enteros.")

def fibonacci(numero):
  if numero < 2:
    return numero
  else:
    return fibonacci(numero - 1) + fibonacci(numero - 2)


print(f"\n{numero} = {fibonacci(numero)}.")
