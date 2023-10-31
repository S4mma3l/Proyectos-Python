"""print("consulta de velocidad")

kilometros = int(input("indique su velocidad actual, Por favor: "))

if kilometros > 80:
    detenido_por = "acceso de velocidad"
else:
    detenido_por = "Adelante"

print(detenido_por)"""


print("consulta de velocidad")

kilometros_maximos = 80


kilometros = int(input("indique su velocidad actual, Por favor: "))

if kilometros > 80:
    detenido_por = "exceso de velocidad"
    print(detenido_por)
    exit()

else:
    buena_conduccion = "Adelante"

    

if kilometros < kilometros_maximos:
    kilometros_maximos = kilometros


# Se leen dos números
"""number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)
"""
