import math

print(math.pi)
print(math.factorial(3))
print(math.sqrt(4))
 
 #1
 
#num = float(input("Dame un número: ")) 
#print(num * 2)

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