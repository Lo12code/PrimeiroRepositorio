lista_desordenada = []


def menor_elemento(lista):
    menor_numero = lista_desordenada[0]
    indice_menor_numero = 0
    for i in range(1, len(lista_desordenada)):
        if lista_desordenada[i] < menor_numero:
            menor_numero = lista_desordenada[i]
            indice_menor_numero = i
    return (menor_numero, indice_menor_numero)

def ordenar_lista(lista):
    lista_ordenada = []
    while len(lista) != 0:
        menor_numero, indice_menor_numero = menor_elemento(lista)
        lista_ordenada.append(menor_numero)
        lista.pop(indice_menor_numero)
    print(lista_ordenada)

def ordenar_lista_sem_repeticao(lista):
    lista_ordenada = []
    while len(lista) != 0:
        menor_numero, indice_menor_numero = menor_elemento(lista)
        print(menor_numero)
        if len(lista_ordenada) == 0:
            lista_ordenada.append(menor_numero)
            continue
        if menor_numero == lista_ordenada[-1]:
            lista.pop(indice_menor_numero)
            continue
        lista_ordenada.append(menor_numero)
        lista.pop(indice_menor_numero)
    print(lista_ordenada)

