
def ordenar_lista(lista):
    return sorted(lista)

def invertir_lista(lista):
    return lista[::-1]

def palindromo_lista(lista):
    if lista == lista[::-1]:
        return True
    return False

def eliminar_duplicados(lista):
    return list(set(lista))

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
