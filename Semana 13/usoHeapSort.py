from heap import *

heap = Heap(5)
heap.tamanio = 5
heap.vector = [11, 3, 81, 7, 45]


monticulizar(heap)
print(heap.vector)
HeapSort(heap)

print(heap.vector)

print(buscar_h(heap, 11))