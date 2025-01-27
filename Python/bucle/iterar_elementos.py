animales =  ["gato","perro","cotorro","pinguino"]
numeros = [10, 20, 30, 40]

for animal in animales: 
    print(f'Ahora la variable animal es igual a: {animal}')
    
#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)
    
for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
#forma que no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el ìndice es: {indice} y el valor es: {valor}')

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else: 
    print("fin del bucle" )   
    
#todo funciona para tuplas y conjuntos