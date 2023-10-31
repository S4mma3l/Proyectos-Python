"""palabra = input("Por favor, ingresa la palabra secreta: ")

while palabra != "cupacabra":
    palabra = input("Por favor, ingresa la palabra secreta: ")

print("has dejado el ciclo con exito")"""

while True:
    palabra = input("Por favor, ingresa la palabra secreta: ")
    if palabra == "cupacabra":
        print("has dejado el ciclo con exito")
        break