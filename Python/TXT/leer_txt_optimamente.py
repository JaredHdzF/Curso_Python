
#Con with open
with open("TXT\\texto.txt",encoding="UTF-8") as archivo:
   
    contenido = archivo.read()
    print(contenido)
    
#no es necesario cerrarlo al usar with open