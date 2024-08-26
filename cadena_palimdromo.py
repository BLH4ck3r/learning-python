print(f"\nCadenas Palindromo\n")

cadena = ''
while True:
  cadena = input("Digite una cadena de text0: ")
  if all(char.isalpha() or char.isspace() for char in cadena):
    break
  else:
    print("[!]Error, solo se aceptan letras. ")

def palindromo(cadena):
  return cadena == cadena[::-1]

if palindromo(cadena):
  print(f"{cadena} si es palindromo")
else:
  print(f"{cadena} no es palindromo")
