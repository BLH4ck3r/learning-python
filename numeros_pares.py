print(f"\nNumeros pares\n")

while True:
  try:
    numero = int(input("Digite un numero entero: "))
    if numero < 0:
      print("[!]Error, solo se aceptan números positivos. ")
      continue
    break
  except ValueError:
    print("[!]Error, solo se aceptan números enteros.")

def es_par(numero):
  return numero % 2 == 0

if es_par(numero):
  print(f"{numero} es par")

else:
  print(f"{numero} es impar")
