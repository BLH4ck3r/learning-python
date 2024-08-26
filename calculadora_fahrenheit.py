print(f"\nCalculadora de °celsius a  °Fahrenheit")

while True:
  try:
    grados = float(input("Digite los grados a calcular: "))
    break
  except ValueError:
    print("[!]Error, solo se aceptan números.")


def calculadora(grados):
  return (grados * 1.8) + 32


print(f"\n{grados}°Celsius = {calculadora(grados)}°Fahrenheit")
