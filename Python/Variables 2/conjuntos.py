#creando un conjunto con set()
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}
print(conjunto2)

conjunto3 = {1,3,5,7}
conjunto4 = {2,4,7,8}

#verificando si es un subconjunto
resultado1 = conjunto2.issubset(conjunto1)
resultado2 = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado3 = conjunto2.issuperset(conjunto1)
resultado4 = conjunto2 > conjunto1

#verificar si hay algùn nùmero en comun
resultado = conjunto3.isdisjoint(conjunto4)

print(resultado)