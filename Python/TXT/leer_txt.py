#Open --> abre archivo con codificacion universal
archivo = open("TXT\\texto.txt",encoding="UTF-8")

#leer linea por linea
lineas = archivo.readlines()

archivo.close()

print(lineas)