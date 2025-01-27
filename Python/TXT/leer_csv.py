import csv

with open("TXT\\datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)