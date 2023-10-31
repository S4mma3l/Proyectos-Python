c0 = int(input("Ingrese un numero (que no sea negativo, ni sea cero): "))
pasos = 0
while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
        if c0 != 1:
            pasos += 1
            print("Nuevo valor", c0)
            continue
        elif c0 == 1:
            pasos += 1
            print("Nuevo valor", c0)
            break
    elif c0 % 2 == 1:
        c0 = c0 * 3 + 1
        if c0 != 1:
            pasos += 1
            print("Nuevo valor", c0)
            continue

print('Total de pasos: ', pasos)