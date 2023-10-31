i = 0
while i < 100:
    # do_something()
    i += 1

for i in range(100):
    # do_something()
    pass

for i in range(6):
    print("El valor de i es", i)

for i in range(2, 8):
    print("El valor de i es", i)

for i in range(2, 8, 3):
    print("El valor de i es", i)

for i in range(1, 1):
    print("El valor de i es", i)

for i in range(2, 1):
    print("El valor de i es", i)

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

import time
for x in range(1,6):
    print(x, "mississippi")
    time.sleep(1)

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

"""largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")"""

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")