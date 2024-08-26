class Calculadora:

  def __init__(self):
    pass

  def suma(self, a, b):
    if a.is_integer() and b.is_integer():
      return f"\nSuma: \n{int(a)} + {int(b)} = {int(a + b)}"
    else:
      return f"\nSuma: \n{a} + {b} = {a + b}"

  def resta(self, a, b):
    if a.is_integer() and b.is_integer():
      return f"\nResta: \n{int(a)} + {int(b)} = {int(a - b)}"
    else:
      return f"\nResta: \n{a} + {b} = {a - b}"

  def multiplicacion(self, a, b):
    if a.is_integer() and b.is_integer():
      return f"\nMultiplicacion: \n{int(a)} + {int(b)} = {int(a * b)}"
    else:
      return f"\nMultiplicacion: \n{a} + {b} = {a * b}"

  def division(self, a, b):
    if b != 0:
      if a.is_integer() and b.is_integer():
        return f"\nDivisión: \n{int(a)} + {int(b)} = {a / b}"
      else:
        return f"\nDivisión: \n{a} + {b} = {a / b}"
    else:
      return "Error: No se puede dividir entre 0"
