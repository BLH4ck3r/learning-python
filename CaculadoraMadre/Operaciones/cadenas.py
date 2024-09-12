
def contar_vocales(cadena):
    contador = 0
    for i in cadena:
        if i.lower() in 'aeiou':
            contador +=1
    return contador

def contar_palabras(cadena):
    a = cadena.split()
    return len(a)
