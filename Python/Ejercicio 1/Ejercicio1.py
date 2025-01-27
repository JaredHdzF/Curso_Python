OC_MAX = 7
OC_MIN = 2.5
OC_PROMEDIO = 4
DAL_C = 1.5

#Duración de video sin edición

C_promedio = 5
C_dal = 3.5

#Diferencias

diferencia_con_min = 100 - (DAL_C / OC_MIN *100)
diferencia_con_max = 100 - (DAL_C / OC_MAX *100)
diferencia_con_prom = 100 - (DAL_C / OC_PROMEDIO *100)
print("-------------")
tiempo_vacío_prom = 100 - OC_PROMEDIO *1000 // C_promedio / 10
tiempo_vacío_dalt = 100 - DAL_C *1000 // C_dal / 10
print("El curso de Dal dura: ")
print(f'- {diferencia_con_min}% menos que el más rápido')
print(f'- {diferencia_con_max}% menos que el más lento')
print(f'- {diferencia_con_prom}% menos que el el promedio')
print("-------------")
print(f'Un curso promedio elimina un {tiempo_vacío_prom}% de tiempo vacío')
print(f'Un curso promedio elimina un {tiempo_vacío_dalt}% de tiempo vacío')    
print("-------------")
print(f'Ver 10 horas de este curso equivale a ver {OC_PROMEDIO * 100  // DAL_C / 10} horas de otro curso') 
print(f'Ver 10 horas de otros cursos equivale a ver {DAL_C * 100  // OC_PROMEDIO / 10} horas de este curso') 