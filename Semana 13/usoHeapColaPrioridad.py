from heap import *
from random import randint

heap = Heap(10)
while not heap_lleno(heap):
    num = randint(0, 500)
    prioridad = randint(1, 3)
    arribo_h(heap, num, prioridad)
while not heap_vacio(heap):
    dato = atencion_h(heap)
    print(dato)
