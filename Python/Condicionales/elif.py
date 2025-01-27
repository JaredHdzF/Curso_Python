ingreso_mensual = 50000
gasto_mensual = 8000

if ingreso_mensual > 10000:
    if gasto_mensual < 7000:
        print("tas joya")
    elif ingreso_mensual - gasto_mensual > 30000:
        print("estás bien")     
    else:
        print("estás mal")
    
elif ingreso_mensual > 1000:
    print("estás bien económicamente en LATAM")
elif ingreso_mensual > 100:
    print("estás bien económicamente en Argentina")
elif ingreso_mensual > 50:
    print("estás bien económicamente en Venezuela")      
else:
    print("eres pobre")
    