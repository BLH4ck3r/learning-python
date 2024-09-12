import math

def es_par(num1):
    return num1 % 2 == 0

def es_primo(num1):
    if num1 <= 2:
        return False
    else:
        for i in range(2, int(math.sqrt(num1) + 1)):
            if num1 % i == 0:
                return False
    return True

def factorial_numero(num1):
    if num1 < 2:
        return 1
    else:
        return num1 * factorial_numero(num1 - 1)

def fibonacci_numero(num1):
    if num1 < 2:
        return num1
    else:
        return fibonacci_numero(num1 - 1) + fibonacci_numero(num1 - 2)
    
def porcentaje_numero(num1, porc):
    return num1 * (porc/100)
