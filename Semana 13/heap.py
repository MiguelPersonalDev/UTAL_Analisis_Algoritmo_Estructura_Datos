from math import inf

class Heap(object):
    def __init__(self, tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio


def intercambio(vector, a, b):
    aux = vector[a]
    vector[a] = vector[b]
    vector[b] = aux


def flotar(heap, indice):
    while indice > 0 and heap.vector[indice] > heap.vector[(indice - 1) // 2]:
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre


def hundir(heap, indice):
    hijo_izq = (indice * 2) + 1
    control = True
    while control and hijo_izq < heap.tamanio:
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if hijo_der < heap.tamanio:
            if heap.vector[hijo_der] > heap.vector[hijo_izq]:
                aux = hijo_der

        if heap.vector[indice] < heap.vector[aux]:
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False


def agregar(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1


def quitar(heap):
    intercambio(heap.vector, 0, heap.tamanio - 1)
    dato = heap.vector[heap.tamanio - 1]
    heap.tamanio -= 1
    hundir(heap, 0)
    return dato


def cantidad_elementos(heap):
    return heap.tamanio


def heap_vacio(heap):
    return heap.tamanio == 0


def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)


def monticulizar(heap):
    for i in range(len(heap.vector)):
        flotar(heap, i)


# para colas con prioridad


def arribo_h(heap, dato, prioridad):
    agregar_h(heap, [prioridad, dato])


def atencion_h(heap):
    return quitar_h(heap)


def cambiar_prioridad(heap, indice, prioridad):
    prioridad_anterior = heap.vector[indice][0]
    heap.vector[indice][0] = prioridad
    if prioridad < prioridad_anterior:
        flotar_h(heap, indice)
    elif prioridad > prioridad_anterior:
        hundir_h(heap, indice)


# para ordenar un vector
def monticulizar(heap):
    for i in range(len(heap.vector)):
        flotar(heap, i)


def HeapSort(heap):
    aux = heap.tamanio
    for i in range(heap.tamanio):
        quitar(heap)
    heap.tamanio = aux


def buscar_h(heap, dato):
    response = None
    for i in range(len(heap.vector)):
      
        if heap.vector[i][1][0] == dato:
            response = i

    return response

def flotar_h(heap, indice):
    while indice > 0 and heap.vector[indice][0] < heap.vector[(indice - 1) // 2][0]:
        padre = (indice - 1) // 2
        intercambio(heap.vector, indice, padre)
        indice = padre

def agregar_h(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar_h(heap, heap.tamanio)
    heap.tamanio += 1


def hundir_h(heap, indice):
    hijo_izq = (indice * 2) + 1
    control = True
    while control and hijo_izq < heap.tamanio:
        hijo_der = hijo_izq + 1
        aux = hijo_izq
        if hijo_der < heap.tamanio:
            if heap.vector[hijo_der][0] < heap.vector[hijo_izq][0]:
                aux = hijo_der

        if heap.vector[indice][0] > heap.vector[aux][0]:
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izq = (indice * 2) + 1
        else:
            control = False


def quitar_h(heap):
    intercambio(heap.vector, 0, heap.tamanio - 1)
    dato = heap.vector[heap.tamanio - 1]
    heap.tamanio -= 1
    hundir_h(heap, 0)
    return dato