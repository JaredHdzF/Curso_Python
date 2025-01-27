#creando diccionarios con dict()
diccionario = dict(nombre="jared",apellido="hernandez")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["jared","aburrido" ]):"jeje"}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "idk"
diccionario = dict.fromkeys(["nombre","apellido"],"idk")

print(diccionario["nombre"])