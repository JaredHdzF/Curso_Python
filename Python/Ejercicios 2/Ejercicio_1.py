#Faltó el maestro y los alumnos harán la clase

#Pedir el nombre y edad de los que asistieron
def obtener_compañeros(cantidad):
    compañeros = []
    for i in range(5):
        nombre = input("ingrese el nombre del compañero: ")
        edad = input("ingrese la edad del compañero: ")
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañeros(3)
print(f'El profesor es: {profesor} y su asistente es: {asistente}')