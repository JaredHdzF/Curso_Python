
#creando una funciòn simple
#def saludar():
#   print("Hola lucas, mi maestro ¿Como andas?")
    
#ejecutando la funcion simple
#saludar()

#crear una funcion con parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "leyenda"
    else:
        adjetivo = 'amor'
    print(f"Hola {nombre}, mi {adjetivo} ¿Como estás?")
saludar("Verlp","mujer")
saludar("jared","hombre")

#crear una funcion que nos retorne multiples valores
def crear_contraseña(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
password,primer_numero = crear_contraseña(697)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña es: {password}")
print(f"El nùmero utilizado para crearla fue: {primer_numero}")




