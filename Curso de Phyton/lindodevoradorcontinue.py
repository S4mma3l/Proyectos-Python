palabra_de_usuario = input("Ingresa una palabra: ") 
palabra_de_usuario = palabra_de_usuario.upper() 


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
        palabra_sin_vocales = letra
        palabra_de_usuario = palabra_sin_vocales

    print(palabra_de_usuario)