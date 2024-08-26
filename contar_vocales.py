print(f"\nContar vocales\n")

cadena = ''
while True:
  cadena = input("Digite una cadena de texto: ")
  if all(char.isalpha() or char.isspace() for char in cadena):
    break
  else:
    print("[!]Error, solo se aceptan letras.")

def contar_vocales(cadena):
  contador = 0
  for i in cadena:
    if i.lower() in 'aeiou':
      contador += 1
  return contador

print(f"{cadena} tiene {contar_vocales(cadena)} vocales")
