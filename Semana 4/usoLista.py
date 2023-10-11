from lista import Lista, insertar, imprimir, tamanio, eliminar

lista = Lista()

insertar(lista, "primero")
insertar(lista, "segundo")
insertar(lista, "tercero")

print("----agregado")
imprimir(lista)

print("----tamaño")
print(tamanio(lista))

print("----eliminado")
print(eliminar(lista, "quinto"))
print(eliminar(lista, "primero"))

print("----fin manipulación")
imprimir(lista)
print("----tamaño")
print(tamanio(lista))

lista2 = Lista()
insertar(lista2, {"id": "1", "nombre": "pepito"})
imprimir(lista2)
