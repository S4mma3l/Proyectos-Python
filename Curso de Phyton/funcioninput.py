# print("Hola, como estas?")
# como_estas = input()
# print(como_estas, "Cuanto, Me alegra!!! ", sep = (",  "))

# anything = input("Dime lo que sea...")
# print("Hmm...", anything, "...¿en serio?")

"""anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)"""

"""
La última línea lo explica todo, se intentó aplicar el operador ** a 'str' (una cadena) acompañado por un 'float'.

Esto está prohibido.

Esto debe de ser obvio. ¿Puedes predecir el valor de "ser o no ser" elevado a la potencia 2?

No podemos. Python tampoco puede.

¿Habremos llegado a un punto muerto? ¿Existirá alguna solución? Claro que la hay.
"""
# Conversion de tipos
"""
Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().

Sus nombres indican cual es su función:

La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; 
si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante);

La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante 
(el resto es lo mismo).
Esto es muy simple y muy efectivo. Sin embargo, estas funciones se pueden invocar directamente pasando 
el resultado de la función input() directamente. No hay necesidad de emplear variables como almacenamiento intermedio.

Se ha implementado esta idea en el editor - observa el código.

¿Puedes imaginar como la cadena introducida por el usuario fluye desde la función input() hacía la función print()?

Intenta ejecutar el código modificado. No olvides introducir un número valido.

Prueba con diferentes valores, pequeños, grandes, negativos y positivos. El cero también es un buen valor a introducir.
"""

# anything = float(input("Ingresa un número: "))
# something = anything ** 2.0
# print(anything, "a la potencia de 2 es", something)

# Más sobre input() y conversión de tipo
""" 
El tener un equipo compuesto por input()-int()-float() abre muchas nuevas posibilidades.

Eventualmente serás capaz de escribir programas completos, los cuales acepten datos en forma de números, los cuales serán procesados y se mostrarán los resultados.

Por supuesto, estos programas serán muy primitivos y no muy utilizables, debido a que no pueden tomar decisiones, y consecuentemente no son capaces de reaccionar acorde a cada situación.

Sin embargo, esto no es un problema; se explicará como solucionarlo pronto.

El siguiente ejemplo hace referencia al programa anterior que calcula la longitud de la hipotenusa. Vamos a reescribirlo, para que pueda leer las longitudes de los catetos desde la consola.

Revisa la ventana del editor - así es como se ve ahora:
"""

# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("La longitud de la hipotenusa es:", hypo)

"""
Este programa le preguntó al usuario los dos catetos, calcula la hipotenusa e imprime el resultado. 
Ejecútalo de nuevo e intenta introducir valores negativos.

El programa desafortunadamente, no reacciona correctamente a este error. Vamos a ignorar esto por ahora. 
Regresaremos a ello pronto.

Toma en cuenta que en el programa que puede ver en el editor, 
la variable hypo se usa con un solo propósito - guardar el valor calculado entre la ejecución de la línea de código contigua.

Debido a que la función print() acepta una expresión como argumento, se puede quitar la variable del código.

Como se muestra en el siguiente código:
"""

# leg_a = float(input("Ingresa la longitud del primer cateto: "))
# leg_b = float(input("Ingresa la longitud del segundo cateto: "))
# print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)

# Operadores Cadena

"""
Es tiempo de regresar a estos dos operadores aritméticos: + y *.

Ambos tienen una función secundaría. Son capaces de hacer algo más que sumar y multiplicar.

Los hemos visto en acción cuando sus argumentos son (flotantes o enteros, no hay diferencia).

Ahora veremos que son capaces también de manejar o manipular cadenas, aunque, en una manera muy específica.

El signo de + (más), al ser aplicado a dos cadenas, se convierte en un operador de concatenación:


string + string
 
Simplemente concatena (junta) dos cadenas en una. Por supuesto, puede ser utilizado más de una vez en una misma expresión, 
y en tal contexto se comporta con enlazado del lado izquierdo.

En contraste con el operador aritmético, el operador de concatenación no es conmutativo, por ejemplo, "ab" + "ba" 
no es lo mismo que "ba" + "ab".

No olvides, si se desea que el signo + sea un concatenador, no un sumador, 
solo se debe asegurar que ambos argumentos sean cadenas.

No se pueden mezclar los tipos de datos aquí.

Este sencillo programa muestra el signo + en su segundo uso:
"""

# fnam = input("¿Me puedes dar tu nombre por favor? ")
# lnam = input("¿Me puedes dar tu apellido por favor? ")
# print("Gracias. ")
# print("\nTu nombre es " + fnam + " " + lnam + ".")

# Replicacion
"""
El signo de * (asterisco), cuando es aplicado a una cadena y a un número (o a un número y cadena) 
se convierte en un operador de replicación:


string * number
number * string
 
Replica la cadena el numero de veces indicado por el número.

Por ejemplo:

"James" * 3 produce "JamesJamesJames"
3 * "an" produce "ananan"
5 * "2" (o "2" * 5) produce "22222" (no 10!)
  Recuerda  
Un número menor o igual a cero produce una cadena vacía.

Este sencillo programa "dibuja" un rectángulo, haciendo uso del antiguo operador (+) en un nuevo rol:
"""

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")


"""a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\n eso es todo, por ahora!")"""


x = float(input("Ingresa el valor para x: "))

y = 1 / (x + 1  / (x + 1 / (x + 1 / x)))

print("y =", y)
