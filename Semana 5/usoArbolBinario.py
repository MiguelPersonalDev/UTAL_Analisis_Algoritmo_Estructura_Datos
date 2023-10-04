from arbol import insertarNodo, eliminarNodo, imprimirInOrden, imprimirPreOrden, imprimirPorNivel

raiz = None

raiz = insertarNodo(raiz,"F")
raiz = insertarNodo(raiz,"B")
raiz = insertarNodo(raiz,"K")
raiz = insertarNodo(raiz,"E")
raiz = insertarNodo(raiz,"H")
raiz = insertarNodo(raiz,"R")
raiz = insertarNodo(raiz,"J")


print("---------preOrden")
imprimirPreOrden(raiz)
print("---------porNivel")
imprimirPorNivel(raiz)
print("---------inOrden")
imprimirInOrden(raiz)

eliminarNodo(raiz,"K")
print("---------porNivel despues de eliminar")
imprimirPorNivel(raiz)