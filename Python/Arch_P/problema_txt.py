#Hacer una lista con nombres y una con apellidos
nombres = ["Jared","Alejandro","José","Adriana","Berenice"]
apellidos = ["Hernández","Figueroa","Curry","López","Ramirez"]

#Registrar en un TXT 

with open("Arch_P\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]
    