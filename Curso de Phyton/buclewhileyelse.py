"""
Ambos bucles while y for, tienen una característica interesante (y rara vez se usa).

Te mostraremos como funciona - intenta juzgar por ti mismo si es utilizable.

En otras palabras, trata de convencerte si la función es valiosa y útil, o solo es azúcar sintáctica.

Echa un vistazo al fragmento en el editor. Hay algo extraño al final - la palabra reservada else.

Como pudiste haber sospechado, los bucles también pueden tener la rama else, como los if.

La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.

¿Puedes adivinar la output? Ejecuta el programa para comprobar si tenías razón.
"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# Modifica el fragmento un poco para que el bucle no tenga oportunidad de ejecutar su cuerpo ni una sola vez:

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

# El bucle for y el bloque else

"""
Los bucles for se comportan de manera un poco diferente - echa un vistazo al fragmento en el editor y ejecútalo.
"""
for i in range(5):
    print(i)
else:
    print("else:", i)

# Modifica el código un poco para realizar un experimento más.
i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

"""
¿Puedes adivinar la output?

El cuerpo del bucle no se ejecutará aquí en absoluto. Nota: hemos asignado la variable i antes del bucle.

Ejecuta el programa y verifica su output.

Cuando el cuerpo del bucle no se ejecuta, la variable de control conserva el valor que tenía antes del bucle.

Nota: si la variable de control no existe antes de que comience el bucle, 
no existirá cuando la ejecución llegue a la rama else branch.

¿Cómo te sientes acerca de esta variante de else?

Ahora vamos a informarte sobre otros tipos de variables. Nuestras variables actuales solo pueden almacenar un valor a la vez, 
pero hay variables que pueden hacer mucho más - pueden almacenar tantos valores como desees. 
Pero primero hagamos algunos laboratorios.
"""