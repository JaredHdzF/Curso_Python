lista = list (["hola", "adios", 30])
cantidad_elementos = len(lista)
print(cantidad_elementos)

#agregar elemento
lista.append("curryOH")

#agregar elemento en un indice específico
lista.insert(2,"bailavini")

#agregar varios elementos
lista.extend([False, 2025])

#eliminar por elemento
lista.pop(-1)

#eliminar todo
lista.clear()

print(lista)