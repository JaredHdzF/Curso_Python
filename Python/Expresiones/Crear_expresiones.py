import re

#detectando un numero CABA y ocultandolo
texto = "Hola verelp, mi numero es: 462 158 9813"

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

remplazo = re.sub(pattern,"(Número oculto)",texto)

print(remplazo)