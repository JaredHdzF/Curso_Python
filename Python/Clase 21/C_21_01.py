print ("hola mundo")
"string" # <-- Es texto
'string'

"""Mis datos son: 
Nombre: Jared
Apellido Hernández"""
''''Mis datos son: 
    Nombre: Jared
    Apellido Hernández'''

#Para acceder a ciertas letras
#Hola =  ("hola mundo")[0:7]
#print(Hola)

#Resultado = "Rojo".upper() == "rojo".upper()
#print(Resultado)
#Resultado2 = "rojo".upper() == "rojo".upper()
#print(Resultado2)

#cadena1 = "hello world"
#print(dir(cadena1))
#resultado3 = cadena1.capitalize()
#print(resultado3)

#Ejercicios

#1

Nombre = "Jared"
Apellido = " Hernández"

Dame_tu_nombre = (Nombre)
print(Dame_tu_nombre) 

caracteres = len(Nombre)
print(f"Tu nombre tiene {caracteres} caracteres.")

#2

Dame_tu_nombre_completo = Nombre + Apellido
print(Dame_tu_nombre_completo)
#O
Dame_tu_nombre_completo_concatenando = "Jared" + " Hernández" 
print(Dame_tu_nombre_completo_concatenando)

caracteres2 = len(Dame_tu_nombre_completo)
print(f"Tu nombre tiene {caracteres2} caracteres.")

#3

nombre = input("Dame tu nombre: ")
if len(nombre) < 5:
    apellido = input("Si tu nombre tiene menos de 5 caracteres, dame tu apellido: ")
    resultado = (nombre + apellido).upper()
else:
    resultado = nombre.lower()
print("Resultado:", resultado)

import math

print(math.pi)
print(math.factorial(3))
print(math.sqrt(4))
 
 #1
 
num = float(input("Dame un número: ")) 
print(num * 2)

#2

numero = float(input("Dame un número: ")) 
raiz = math.sqrt(numero)
raíz_dos_decimales = round(raiz, 2)
print(f"La raíz cuadrada de {numero} es aproximadamente {raíz_dos_decimales}.")

#3

pi_cinco_decimales = round(math.pi, 5)
print(pi_cinco_decimales)

#4

radio = float(input("Dame el radio: "))
area = math.pi * (radio ** 2)
print(f"El área con radio {radio} es {area}.")

radio2 = float(input("Dame el radio: "))
altura = float(input("Dame la altura: "))
area2 = altura * (math.pi * (radio ** 2))
print(f"El área del cilindro con radio {radio} y altura {altura} es {area2}.")

