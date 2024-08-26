print(f"\nCadena inversa\n")

cadena = ''
while True:
  cadena = input("Digite una cadena de texto: ")
  if all(char.isalpha() or char.isspace() for char in cadena):
    break
  else:
    print("[!]Error, solo se aceptan letras.")


def inversa(cadena):
  return cadena[::-1]


print(f"\nNormal: {cadena}")
print(f"\nInvertida: {inversa(cadena)}")
