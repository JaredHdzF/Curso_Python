frutas = ["banana","manzana","ciruela","pera","naranja"]
cadena = "Hola jared"
numeros = [1,3,5,7]

#evitando una variable 
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')
    
#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break
else: 
    print("terminado")
    
for letra in cadena:
    print(letra)
    
#for en una sola linea de còdigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)