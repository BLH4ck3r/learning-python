import math

print(f"\nNumeros Primos\n")

while True:
  try:
    numero = int(input("Digite un numero entero: "))
    if numero < 0:
      print("[!]Error, solo se aceptan números positivos. ")
      continue
    break
  except ValueError:
    print("[!]Error, solo se aceptan números enteros.")


def es_primo(numero):
  if numero <= 2:
    return False
  else:
    for i in range(2, int(math.sqrt(numero) + 1)):
      if numero % i == 0:
        return False
  return True

if es_primo(numero):
  print(f"\n{numero} es primo")
else:
  print(f"\n{numero} no es primo")
