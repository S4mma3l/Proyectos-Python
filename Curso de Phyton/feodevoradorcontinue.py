palabra_de_usuario = input("Ingresa una palabra: ") # Indicar al usuario que ingrese una palabra
palabra_de_usuario = palabra_de_usuario.upper() # y asignarlo a la variable user_word. upper para convertir a mayusculas

for letra in palabra_de_usuario:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        print(letra)
    # Completa el cuerpo del bucle for.