class Calculadora:#clase Calculadora

  def __init__(self):#constructor
    pass

  def suma(self, a, b):#funcion suma
    if a.is_integer() and b.is_integer():#validamos que los datos ingresados sean enteros
      return f"\nSuma: \n{int(a)} + {int(b)} = {int(a + b)}"#el resultado se retornará como entero
    else:
      return f"\nSuma: \n{a} + {b} = {a + b}"#el resultado se retornará como flotante

  def resta(self, a, b):#funcion resta
    if a.is_integer() and b.is_integer():
      return f"\nResta: \n{int(a)} + {int(b)} = {int(a - b)}"
    else:
      return f"\nResta: \n{a} + {b} = {a - b}"

  def multiplicacion(self, a, b):#funcion multiplicacion
    if a.is_integer() and b.is_integer():
      return f"\nMultiplicacion: \n{int(a)} + {int(b)} = {int(a * b)}"
    else:
      return f"\nMultiplicacion: \n{a} + {b} = {a * b}"

  def division(self, a, b):#funcion division
    if b != 0:#validamos que el segundo numero sea diferente de 0
      if a.is_integer() and b.is_integer():
        return f"\nDivisión: \n{int(a)} + {int(b)} = {a / b}"
      else:
        return f"\nDivisión: \n{a} + {b} = {a / b}"
    else:
      return "Error: No se puede dividir entre 0"#retornamos un mensaje de error
