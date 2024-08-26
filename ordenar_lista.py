print(f"\nOrdenamiento de lista\n")

lista = []
while True:
  try:
    cantidad = int(input("Digite la cantidad de ítems que tendrá la lista: "))
    if cantidad < 0:
      print("[!]Error, solo se aceptan números positivos.")
    break
  except ValueError:
    print("[!]Error, solo se aceptan números enteros.")

for i in range(cantidad):
  while True:
    try:
      numeros = int(input(f"[{i+1}].Digite un numero: "))
      lista.append(numeros)
      if numeros < 0:
        print("[!]Error, solo se aceptan números positivos.")
      break
    except ValueError:
      print("Error, solo se aceptan números enteros.")

def es_ordenada(lista):
  return lista == sorted(lista)


if es_ordenada(lista):
  print(f"\n {lista} Esta lista ya esta ordenada.")

else:
  print(f"\nLista normal = {lista} \nLista Ordenada = {sorted(lista)}")
