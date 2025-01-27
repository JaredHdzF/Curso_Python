import re

# La cadena en la que se buscarán los patrones
text = "La fecha es 25/01/2025 y el teléfono es +462 158 98 13"

# El patrón a buscar
pattern = r"\d{2}/\d{2}/\d{4}"

# El texto con el que se reemplazará el patrón
replacement = "Fecha oculta"

# Reemplazar todas las apariciones del patrón en la cadena de texto
new_text = re.sub(pattern, replacement, text)

print("Texto modificado:", new_text)