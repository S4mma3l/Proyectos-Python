# Bucles con while
"""
¿Estás de acuerdo con la sentencia presentada a continuación?

mientras haya algo que hacer
    hazlo
 
Toma en cuenta que este registro también declara que, si no hay nada que hacer, nada ocurrirá.

En general, en Python, un bucle se puede representar de la siguiente manera:

while
    instruction
 
Si observas algunas similitudes con la instrucción if, está bien. De hecho, la diferencia sintáctica es solo una: 
usa la palabra while en lugar de la palabra if.

La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus sentencias sólo una vez; 
while repite la ejecución siempre que la condición se evalúe como True.

Nota: todas las reglas relacionadas con sangría también se aplican aquí. Te mostraremos esto pronto.

Observa el algoritmo a continuación:

while conditional_expression:
    instruction_one
    instruction_two
    instruction_three
    :
    :
    instruction_n
 
Ahora, es importante recordar que:

si deseas ejecutar más de una sentencia dentro de un while, debes (como con if) poner sangría a todas las instrucciones 
de la misma manera.
una instrucción o conjunto de instrucciones ejecutadas dentro del while se llama el cuerpo del bucle.
si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, el cuerpo no se ejecuta ni una sola vez 
(ten en cuenta la analogía de no tener que hacer nada si no hay nada que hacer).
el cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al principio, 
el cuerpo podría funcionar continuamente hasta el infinito. Observa que hacer una cosa generalmente disminuye 
la cantidad de cosas por hacer.
"""

# Bucle infinito

"""
Un bucle infinito, también denominado bucle sin fin, es una secuencia de instrucciones en un programa que se repite indefinidamente 
(bucle sin fin).

Este es un ejemplo de un bucle que no puede finalizar su ejecución:
"""

"""while True:
    print("Estoy atrapado dentro de un bucle.")"""

"""# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number)"""

# El bucle while: más ejemplos
"""
Veamos otro ejemplo utilizando el bucle while. Sigue los comentarios para descubrir la idea y la solución.
"""
# Un programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares.
# El programa termina cuando se ingresa un cero.

odd_numbers = 0
even_numbers = 0

# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))

# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

"""
Ciertas expresiones se pueden simplificar sin cambiar el comportamiento del programa.

Intenta recordar cómo Python interpreta la verdad de una condición y ten en cuenta que estas dos formas son equivalentes:

while number != 0: y while number:.

La condición que verifica si un número es impar también puede codificarse en estas formas equivalentes:

if number % 2 == 1: y if number % 2:.
"""

# Empleando una variable counter para salir del bucle
"""
ver program counter.py
"""

# Bucles en tu codigo con for
"""
Otro tipo de bucle disponible en Python proviene de la observación de que a veces es más importante contar los
 "giros o vueltas" del bucle que verificar las condiciones.

Imagina que el cuerpo de un bucle debe ejecutarse exactamente cien veces. 
Si deseas utilizar el bucle while para hacerlo, puede tener este aspecto:

ver codigo for.py

Sería bueno si alguien pudiera hacer esta cuenta aburrida por ti. ¿Es eso posible?

Por supuesto que lo es - hay un bucle especial para este tipo de tareas, y se llama for.

En realidad, el bucle for está diseñado para realizar tareas más complicadas, puede "explorar" grandes colecciones de datos elemento por elemento. Te mostraremos como hacerlo pronto, pero ahora presentaremos una variante más sencilla de su aplicación.

Observa el fragmento de código:

ver codigo for.py


Existen algunos elementos nuevos. Déjanos contarte sobre ellos:

la palabra reservada for abre el bucle for; nota - No hay condición después de eso; no tienes que pensar en las condiciones, 
ya que se verifican internamente, sin ninguna intervención.
cualquier variable después de la palabra reservada for es la variable de control del bucle; cuenta los giros del bucle y 
lo hace automáticamente.
la palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la 
variable de control.
la función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; 
en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.
nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía - 
la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo 
(por cierto - if, elif, else y while expresan lo mismo).
Nuestros próximos ejemplos serán un poco más modestos en el número de repeticiones de bucle.

Echa un vistazo al fragmento de código. ¿Puedes predecir su output?

ver codigo for.py

Nota:

El bucle se ha ejecutado diez veces (es el argumento de la función range())
El valor de la última variable de control es 9 (no 10, ya que comienza desde 0 , no desde 1)


La invocación de la función range() puede estar equipada con dos argumentos, no solo uno:
ver codigo for.py

En este caso, el primer argumento determina el valor inicial (primero) de la variable de control.

El último argumento muestra el primer valor que no se asignará a la variable de control.

Nota: la función range() solo acepta enteros como argumentos y genera secuencias de enteros.

¿Puedes adivinar la output del programa? Ejecútalo para comprobar si ahora también estabas en lo cierto.

El primer valor mostrado es 2 (tomado del primer argumento de range()).

El último es 7 (aunque el segundo argumento de range() es 8)

"""

# Bucle for y la funcion range en tre argumentos

"""
La función range() también puede aceptar tres argumentos: Echa un vistazo al código del editor.
ver codigo for.py

El tercer argumento es un incremento - es un valor agregado para controlar la variable en cada giro del bucle 
(como puedes sospechar, el valor predeterminado del incremento es 1).

¿Puedes decirnos cuántas líneas aparecerán en la consola y qué valores contendrán?

Ejecuta el programa para averiguar si tenías razón.

Deberías poder ver las siguientes líneas en la ventana de la consola:
El valor de i es 2
El valor de i es 5
Output
¿Sabes por qué? El primer argumento pasado a la función range() nos dice cual es el número de inicio de la secuencia 
(por lo tanto 2 en la output). El segundo argumento le dice a la función dónde detener la secuencia (la función genera números hasta el número indicado por el segundo argumento, pero no lo incluye). Finalmente, el tercer argumento indica el paso, que en realidad significa la diferencia entre cada número en la secuencia de números generados por la función.

2 (número inicial) → 5 (2 incremento por 3 es igual a 5 - el número está dentro del rango de 2 a 8) → 8 
(5 incremento por 3 es igual a 8 - el número no está dentro del rango de 2 a 8, porque el parámetro de parada no está incluido en la secuencia de números generados por la función).
Nota: si el conjunto generado por la función range() está vacío, el bucle no ejecutará su cuerpo en absoluto.

Al igual que aquí - no habrá output:
ver codigo for.py

Nota: el conjunto generado por range() debe ordenarse en un orden ascendente. No hay forma de forzar el range() 
para crear un conjunto en una forma diferente. Esto significa que el segundo argumento de range() debe ser mayor que el primero.

Por lo tanto, tampoco habrá output aquí:
ver codigo for.py

Echemos un vistazo a un programa corto cuya tarea es escribir algunas de las primeras potencias de dos:

ver codigo for.py

La variable expo se utiliza como una variable de control para el bucle e indica el valor actual del exponente. 
La propia exponenciación se sustituye multiplicando por dos. Dado que 2 0 es igual a 1, 
después 2 × 1 es igual a 21, 2 × 21 es igual a 22, y así sucesivamente. 
¿Cuál es el máximo exponente para el cual nuestro programa aún imprime el resultado?

Ejecuta el código y verifica si la output coincide con tus expectativas.


"""

# lab fundamentos del bucle for
"""
scenario
¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. 
El río Mississippi tiene aproximadamente 2,340 millas de largo, lo que lo convierte en el segundo río más largo de los 
Estados Unidos (el más largo es el río Missouri). ¡Es tan largo que una sola gota de agua necesita 90 días para recorrer 
toda su longitud!

La palabra Mississippi también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que suene más 
cercano al reloj, y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente unos tres segundos 
reales de tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.

Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. 
Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"

Utiliza el esqueleto que hemos proporcionado en el editor.

  INFO EXTRA  
Ten en cuenta que el código en el editor contiene dos elementos que pueden no ser del todo claros en este momento: la sentencia import time y el método sleep(). Vamos a hablar de ellos pronto.

Por el momento, nos gustaría que supieras que hemos importado el módulo time y hemos utilizado el método sleep() 
para suspender la ejecución de cada función posterior de print() dentro del bucle for durante un segundo, 
de modo que el mensaje enviado a la consola se parezca a un conteo real. No te preocupes - 
pronto aprenderás más sobre módulos y métodos.

Salida esperada:

1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
"""

# Sentencia break y continue
"""
Hasta ahora, hemos tratado el cuerpo del bucle como una secuencia indivisible e inseparable de instrucciones que se 
realizan completamente en cada giro del bucle. 
Sin embargo, como desarrollador, podrías enfrentar las siguientes opciones:

parece que no es necesario continuar el bucle en su totalidad; se debe abstener de seguir ejecutando 
el cuerpo del bucle e ir más allá;
parece que necesitas comenzar el siguiente giro del bucle sin completar la ejecución del turno actual.
Python proporciona dos instrucciones especiales para la implementación de estas dos tareas. 
Digamos por razones de precisión que su existencia en el lenguaje no es necesaria - un programador 
experimentado puede codificar cualquier algoritmo sin estas instrucciones. Tales adiciones, que no mejoran el poder
 expresivo del lenguaje, sino que solo simplifican el trabajo del desarrollador, a veces se denominan dulces sintácticos o
   azúcar sintáctica.

Estas dos instrucciones son:

break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle; 
el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.
continue - se comporta como si el programa hubiera llegado repentinamente al final del cuerpo; 
el siguiente turno se inicia y la expresión de condición se prueba de inmediato.
Ambas palabras son palabras clave reservadas.

Ahora te mostraremos dos ejemplos simples para ilustrar como funcionan las dos instrucciones. 
Mira el código en el editor. Ejecuta el programa y analiza la output. Modifica el código y experimenta.

ver codigo for.py

"""
"""
Las sentencias break y continue: más ejemplos
Regresemos a nuestro programa que reconoce el más grande entre los números ingresados. 
Lo convertiremos dos veces, usando las instrucciones de break y continue.

Analiza el código y determina como las usarías.

La variante empleando break es la siguiente:
"""
"""

Ejecútalo, pruébalo y experimenta con él.

Y ahora la variante con continue:
ver codigo for.py

Observa con atención, el usuario ingresa el primer número antes de que el programa ingrese al bucle while. 
El número siguiente se ingresa cuando el programa ya está en el bucle.

De nuevo - ejecútalo, pruébalo y experimenta con él.

"""