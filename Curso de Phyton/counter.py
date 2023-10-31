counter = 10
while counter != 0:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

# Pero hay una cosa que se puede escribir de forma más compacta - la condición del bucle while

counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)


print(
    """
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
"""
)


tu_numero = int(input("por favor ingresa el numero secreto: "))
secret_number = 777

while tu_numero != secret_number:
    print("jajajaja! estas atrapado en mi bucle")
    int(input("intenta de nuevo mi numero secreto: "))
print("bien, hecho has adivinado mi numero!!!")
