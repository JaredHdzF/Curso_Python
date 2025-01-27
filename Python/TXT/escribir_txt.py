with open('TXT\\texto.txt','w',encoding="UTF-8") as archivo:
    #sobreescribiendo el archivo
    #archivo.write("Jajajajaa")
    
    #agregando 2 lineas con writelines
    archivo.writelines([" - Hola\n"," - misericordia\n"])
    
    #agregando otras 2 lineas
    archivo.writelines([" - no se porque dijiste eso\n"," - ni yo"])