#Crear una función que nos de la serie de fibonacci hasta el numero indicado

def fibonacci(num):
    a,b =0,1
    fibonacci_lista = []
    for i in range(num):
        if b > num: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b = b,a+b
    return num    

resultado = fibonacci(34)
print(resultado)