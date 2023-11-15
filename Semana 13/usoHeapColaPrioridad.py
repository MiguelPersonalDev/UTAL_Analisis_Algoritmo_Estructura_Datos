from heap import *
from random import randint

heap = Heap(10)
while not heap_lleno(heap):
    num = randint(0, 500)
    prioridad = randint(1, 3)
    arribo(heap, num, prioridad)
print(heap.vector)
while not heap_vacio(heap):
    dato = atencion(heap)
    print(dato)
