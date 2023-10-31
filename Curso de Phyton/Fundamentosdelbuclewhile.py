bloque = int(input("Ingresa el numero de bloques: "))

altura = 0
niveles = 1
while niveles <= bloque:
    altura += 1
    bloque -= niveles
    niveles += 1
print("La altura de la piramide es: ", altura)