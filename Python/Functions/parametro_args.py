#forma no optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,9,10,20,3])

#forma optima
def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([2,4,6,8,10])

#opción 2
def suma(nombre,*numeros):
    return f"{nombre}, la suma es: {sum(numeros)}"
    
resultado = suma("jared",1,3,5,7,9,0)
