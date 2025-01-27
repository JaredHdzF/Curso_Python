#1

nombre = input("Dame tu nombre: ")
for i in range (3):
    print(nombre)
    
#2
    
numero = int(input("Dame un numero: "))
for i in range (numero):
    print(nombre)
    
#3

for letra in nombre:
    print(letra)

#4
repeticiones = int(input("Cuántas veces quieres repetir el código: "))
print(repeticiones) 

for _ in range(repeticiones):
    for letra in nombre:
        print(letra)
    print("------")
    
 
