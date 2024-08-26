print(f"\nBusqueda Binaria\n")

lista = []
while True:
  try:
    cantidad = int(input("Digite la cantidad de ítems para la lista: "))
    if cantidad < 0:
      print("[!]Error, solo se aceptan números positivos. ")
    break
  except ValueError:
    print("[!]Error, solo se aceptan números enteros.")

for i in range(cantidad):
  while True:
    try:
      numeros = int(input(f"[{i+1}].Digite un numero: "))
      if numeros < 0:
        print("[!]Error, solo se aceptan números positivos.")
        continue
      break
    except ValueError:
      print("[!]Error, solo se aceptan números enteros.")
  lista.append(numeros)

while True:
  try:
    objetivo = int(input("Digite el numero a buscar: "))
    if objetivo < 0:
      print("[!]Error, solo se aceptan números positivos.")
    break
  except ValueError:
    print("[!]Error, solo se aceptan números enteros.")

lista.sort()

def busqueda_binaria(lista, objetivo):
  inicio = 0
  fin = len(lista) - 1
  while inicio <= fin:
    medio = (inicio + fin) // 2
    if lista[medio] == objetivo:
      return medio
    elif lista[medio] < objetivo:
      inicio += 1
    else:
      fin -= 1
  return -1

print(f"Fila ordenada: {lista}")

if busqueda_binaria(lista, objetivo) != -1:
  print(
      f"\nEl numero {objetivo} se encuentra en el índice {busqueda_binaria(lista, objetivo)} de la fila."
  )
else:
  print(f"\nEl numero {objetivo} no se encuentra en la fila")
