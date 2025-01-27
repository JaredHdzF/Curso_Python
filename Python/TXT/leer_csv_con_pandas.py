import pandas as pd

df = pd.read_csv("TXT\\datos.csv")
df2 = pd.read_csv("TXT\\datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

#ordeandolo de forma descendente
df_orden_descendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primeras 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las últimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadística del dataframe:
df_info = df.describe()

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todos los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todos los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 2o con loc
mayor_que_20 = df.loc[df["edad"]>20,:]

print(mayor_que_20)




