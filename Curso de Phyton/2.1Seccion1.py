print("Hola, Mundo!")
print("La Witsi Witsi Araña subió a su telaraña.")
print("Vino la lluvia y se la llevó.")

# se puede realizar una salto de linea asi
print("La Witsi Witsi Araña subió a su telaraña.")
print()
print("Vino la lluvia y se la llevó.")

# tambien de esta manera
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")
print()
# el salto de linea se representa de la siguiente forma: /n
# dentro de una funcion como print se puede representar un salto de linea de la siguiente manera: print("\\"")
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print("\\")
print("Vino la lluvia\ny se la llevó.")
# Para realizar un comentario en phyton se puede usar las siguientes opciones
"""Esta forma se realiza cuando el comentario va a requerir mas de una linea
funciona para comentarios extensos"""
print("La Witsi Witsi Araña", "subió", "a su telaraña.")
print()

print("Mi nombre es", "Python.")
print("Monty Python.")
print()

# Argumentos de palabras clave
# Argumento "end"
print("Mi nombre es", "Python.", end=" ")
print("Monty Python.")
print("Mi nombre es", "Python.", end="\n")
print("Monty Python.")
"""La función print() tiene dos argumentos de palabra clave que puedes usar para tus propósitos. El primero se llama end.
En la ventana del editor puedes ver un ejemplo muy simple de cómo usar un argumento de palabra clave.
Un argumento de palabra clave consta de tres elementos: una palabra clave se identifica el argumento (end aquí); un signo de igual (=); y un valor asignado a ese argumento;
cualquier argumento de palabra clave debe colocarse después del último argumento posicional (esto es muy importante)"""

# Argumento "sep"

print("Mi", "nombre", "es", "Monty", "Python.", sep="-")

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")
print()


print("Programming", "Essentials", "in", sep="***", end="...")
print("Python")

# Practica con print Flecha

print()
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")


""" Resumen de la seccion


1. La función print() es una función integrada imprime/envía un mensaje específico a la pantalla/ventana de consola.

2. Las funciones integradas, al contrario de las funciones definidas por el usuario, están siempre disponibles y no tienen que ser importadas. Python 3.7.1 viene con 69 funciones incorporadas. Puedes encontrar su lista completa en orden alfabético en Python Standard Library.

3. Para llamar a una función (invocación de función), debe utilizarse el nombre de la función seguido de un paréntesis. Puedes pasar argumentos a una función colocándolos dentro de los paréntesis. Se deben separar los argumentos con una coma, por ejemplo, print("¡Hola,", "Mundo!"). Una función print() "vacía" imprime una línea vacía a la pantalla.

4. Las cadenas de Python están delimitadas por comillas, por ejemplo, "Soy una cadena" (comillas dobles), o 'Yo soy una cadena, también' (comillas simples).

5. Los programas de computadora son colecciones de instrucciones. Una instrucción es un comando para realizar una tarea específica cuando se ejecuta, por ejemplo, para imprimir un determinado mensaje en la pantalla.

6. En las cadenas de Python la barra diagonal inversa (\) es un carácter especial que anuncia que el siguiente carácter tiene un significado diferente, por ejemplo, \n (el carácter de nuevalínea) comienza una nuevalínea de salida.

7. Los argumentos posicionales son aquellos cuyo significado viene dictado por su posición, por ejemplo, el segundo argumento se emite después del primero, el tercero se emite después del segundo, etc.

8. Los argumentos de palabra clave son aquellos cuyo significado no está dictado por su ubicación, sino por una palabra especial (palabra clave) que se utiliza para identificarlos.

9. Los parámetros end y sep se pueden usar para dar formato la salida de la función print(). El parámetro sep especifica el separador entre los argumentos emitidos. Por ejemplo, print("H", "E", "L", "L", "O", sep="-"), mientras que el parámetro end especifica que imprimir al final de la declaración de impresión.
"""

print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")

# print(sep="&", "fish", "chips") esta instrucion es erronea los argumentos deben de estar despues
print("fish", "chips", sep="&")
print()

print("Greg's book.")
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg's book.")

# literales los datos en si mismos
"""Y esta es la pista: 123 es un literal, y c no lo es.

Se utilizan literales para codificar datos y ponerlos dentro del código. 
Ahora mostraremos algunas convenciones que se deben seguir al utilizar Python."""
# Numeros enteros

print("123")
print(123)
print(0o123)  # Numeros Octales
print(0x123)  # Numero Hexadecimales

# numeros flotantes

""" Nota: dos punto cinco se ve normal cuando se escribe en un programa, sin embargo si tu idioma nativo prefiere el uso de una coma en lugar de un punto, se debe asegurar que el número no contenga comas.

Python no lo aceptará, o (en casos poco probables) puede malinterpretar el número, debido a que la coma tiene su propio significado en Python.

Si se quiere utilizar solo el valor de dos punto cinco, se debe escribir como se mostró anteriormente. Nota que: hay un punto entre el 2 y el 5, no una coma.

Como puedes imaginar, el valor de cero punto cuatro puede ser escrito en Python como:

0.4
Pero no hay que olvidar esta sencilla regla - se puede omitir el cero cuando es el único dígito antes del punto decimal.

En esencia, el valor 0.4 se puede escribir como: .4 o este ejemplo tambien aplica 4.
"""
# Enteros y flotantes

"""en Phyton se se definen los nuemros por enteros o flotantes de la suiente manera:
4 es un numero entero y 4.0 es un numero flotante, tambien se puede utilizar la letra (e)
en Phyton se puede usar la notacion cientifica como por ejemplo para este numero 300000000
que se puede expresar de la siguente manera 3x10elevado a la octava potencia
en Phyton se puede representar asi 3E8 o asi 3e8 se puede escribir la letra en mayuscula o minuscula ya que proviende de la palabra exponente 
Nota:

El exponente (el valor después de la E) debe ser un valor entero;
La base (el valor antes de la E) puede ser un valor entero o flotante.
"""

# Codigo flotante
print("esta es la constante de planck:")
print(6.62607e-34)

# Cadenas
"""las cadenas requeiren comillas asi como los flotantes requeiren punto decimal
supongamos que queremos mostrar el siguente texto: Me gusta "monty Python"
"""

# existen 2 opciones

print(
    'Me gusta "Monty Python"'
)  # con la diagonal invertida o con el concepto de caracter de escape el codigo seria aso: print("Me gusta \"Monty Python\"")

print('Me gusta "Monty Python"')  # o con apostrofe '

# Codificando cadenas
"""que sucede cuando existe un apostrofe ejemplo: i'm Monty Python. la solucion seria la siguiente
codigo print('I\'m Monty Python') si el sistema no tiene correcto
"""

print("I'm Monty Python.")
# una cadena vacia sigue siendo una cade '' o ""

# valores Booleanos
"""El nombre proviene de George Boole (1815-1864), el autor de Las Leyes del Pensamiento, las cuales definen el Álgebra Booleana - una parte del álgebra que hace uso de dos valores: True y False, denotados como 1 y 0.

Un programador escribe un programa, y el programa hace preguntas. Python ejecuta el programa, y provee las respuestas. El programa debe ser capaz de reaccionar acorde a las respuestas recibidas.

Afortunadamente, las computadoras solo conocen dos tipos de respuestas:

Si, esto es verdad.
No, esto es falso.
Nunca habrá una respuesta como: No lo sé o probablemente si, pero no estoy seguro.

Python, es entonces, un reptil binario.

Estos dos valores booleanos tienen denotaciones estrictas en Python:

$True
$False

"""
print(True > False)
print(False < True)

# Practica

print('"Estoy"')
print('""aprendiendo""')
print('"""Python"""')


# Resumen
"""
1. Los literales son notaciones para representar valores fijos en el código. Python tiene varios tipos de literales - es decir, un literal puede ser un número por ejemplo, 123), o una cadena (por ejemplo, "Yo soy un literal.").

2. El sistema binario es un sistema numérico que emplea 2 como su base. Por lo tanto, un número binario está compuesto por 0s y 1s únicamente, por ejemplo, 1010 es 10 en decimal.

Los sistemas de numeración Octales y Hexadecimales son similares pues emplean 8 y 16 como sus bases respectivamente. El sistema hexadecimal utiliza los números decimales más seis letras adicionales.

3. Los enteros (o simplemente int) son uno de los tipos numéricos que soporta Python. Son números que no tienen una parte fraccionaria, por ejemplo, 256, o -1 (enteros negativos).

4. Los números punto-flotante (o simplemente flotantes) son otro tipo numérico que soporta Python. Son números que contienen (o son capaces de contener) una parte fraccionaria, por ejemplo, 1.27.

5. Para codificar un apóstrofe o una comilla dentro de una cadena se puede utilizar el carácter de escape, por ejemplo, 'I\'m happy.', o abrir y cerrar la cadena utilizando un conjunto de símbolos distintos al símbolo que se desea codificar, por ejemplo, "I'm happy." para codificar un apóstrofe, y 'El dijo "Python", no "typhoon"' para codificar comillas.

6. Los valores booleanos son dos objetos constantes True y False empleados para representar valores de verdad (en contextos numéricos 1 es True, mientras que 0 es False.


Extra  

Existe un literal especial más utilizado en Python: el literal None. Este literal es llamado un objeto de NoneType, y puede ser utilizado para representar la ausencia de un valor. Pronto se hablará más acerca de ello.
"""
# Cuestionario de seccion

"""
Pregunta 1: ¿Qué tipos de literales son los siguientes dos ejemplos?

"Hola ", "007"
$Ambos son literales de cadena.

Pregunta 2: ¿Qué tipos de literales son los siguientes cuatro ejemplos?

"1.5", 2.0, 528, False
$El primero es una cadena, el segundo es un literal numérico (un flotante), el tercero es un literal numérico (un entero) y el cuarto es un literal booleano.

Pregunta 3: ¿Cuál es el valor decimal del siguiente número binario?

1011
$es 11, porque 8/4/2/1
             1  0  1  1
             8  0  2  1=11
"""
my_list = [1, 2]

# 2.3
"""python como una calculadora"""

print(2 + 2)

"""Operadores basicos 
+ Simbolo de suma
- simbolo de resta
* simbolo de multiplicacion
/ simbolo de division
// simbolo de division entera
% simbolo de residuo (modulo)
** simbolo de exponenciacion
"""
print(2**3)  # Exponenciacion
print(2**3.0)
print(2.0**3)
print(2.0**3.0)

print(2 * 3)  # Multiplicacion
print(2 * 3.0)
print(2.0 * 3)
print(2.0 * 3.0)

print(6 / 3)  # Division
print(6 / 3.0)
print(6.0 / 3)
print(6.0 / 3.0)

print(6 // 3)  # Division Entera
print(6 // 3.0)
print(6.0 // 3)
print(6.0 // 3.0)

print(-6 // 4)
# El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada.
# Esto es muy importante: el redondeo siempre va hacia abajo.
print(6.0 // -4)

print(14 % 4)  # Residuo

# El siguiente ejemplo es un poco más complicado:

print(12 % 4.5)
"""nota 
3.0 – no 3 pero 3.0. La regla aun funciona:

12 // 4.5 da 2.0,
2.0 * 4.5 da 9.0,
12 - 9.0 da 3.0.

Como no dividir
Como probablemente sabes, la división entre cero no funciona.

No intentes:

Dividir entre cero;
Realizar una división entera entre cero;
Encontrar el residuo de una división entre cero.
"""

print(-4 + 4)  # Suma
print(-4.0 + 8)

print(-4 - 4)  # Resta
print(4.0 - 8)
print(-1.1)

# Por cierto: también hay un operador + unario. Se puede utilizar de la siguiente manera:

print(+2)

# 2.3.3 Operadores y sus prioridades
"""2 + 3 *5
Seguramente recordarás que primero se debe multiplicar 3 por 5, 
mantener el 15 en tu memoria y después sumar el 2, 
dando como resultado el 17.
"""

# Operadores y sus enlaces
"""El enlace de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad, 
los cuales se encuentran dentro de una misma expresión."""

print(9 % 6 % 2)

"""
Existen dos posibles maneras de evaluar la expresión:

De izquierda a derecha: primero 9 % 6 da como resultado 3, y entonces 3 % 2 da como resultado 1;
De derecha a izquierda: primero 6 % 2 da como resultado 0, y entonces 9 % 0 causa un error fatal.
"""

print(9 % 6 % 2)
print(2**2**3)
print(-(3**2))
print(-(2**3))
print(-(3**2))

"""

Prioridad	Operador	
1	**	
2	+, - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza.)	unario
3	*, /, //, %	
4	+, -	binario
"""

print(2 * 3 % 5)

# Operadores y parentesis

"""
Por supuesto, se permite hacer uso de paréntesis, lo cual cambiará el orden natural del cálculo de la operación.

De acuerdo con las reglas aritméticas, las sub-expresiones dentro de los paréntesis siempre se calculan primero.

Se pueden emplear tantos paréntesis como se necesiten, y seguido son utilizados para mejorar la legibilidad de una expresión, aun si no cambian el orden de las operaciones.

Un ejemplo de una expresión con múltiples paréntesis es la siguiente:

"""

print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# Resumen

"""
Puntos Clave
1. Una expresión es una combinación de valores (o variables, operadores, llamadas a funciones, aprenderás de ello pronto) las cuales son evaluadas y dan como resultado un valor, por ejemplo, 1 + 2.

2. Los operadores son símbolos especiales o palabras clave que son capaces de operar en los valores y realizar operaciones matemáticas, por ejemplo, el * multiplica dos valores: x * y.

3. Los operadores aritméticos en Python: + (suma), - (resta), * (multiplicación), / (división clásica: regresa un flotante siempre), % (módulo: divide el operando izquierdo entre el operando derecho y regresa el residuo de la operación, por ejemplo, 5 % 2 = 1), ** (exponenciación: el operando izquierdo se eleva a la potencia del operando derecho, por ejemplo, 2 ** 3 = 2 * 2 * 2 = 8), // (división entera: retorna el número resultado de la división, pero redondeado al número entero inferior más cercano, por ejemplo, 3 // 2.0 = 1.0)

4. Un operador unario es un operador con solo un operando, por ejemplo, -1, o +3.

5. Un operador binario es un operador con dos operandos, por ejemplo, 4 + 5, o 12 % 5.

6. Algunos operadores actúan antes que otros, a esto se le llama - jerarquía de prioridades:

El operador ** (exponencial) tiene la prioridad más alta;
Posteriormente los operadores unarios + y - (nota: los operadores unarios a la derecha del operador exponencial enlazan con mayor fuerza, por ejemplo 4 ** -1 es igual a 0.25)
Después *, /, //, y %,
Finalmente, la prioridad más baja: los operadores binarios + y -.
7. Las sub-expresiones dentro de paréntesis siempre se calculan primero, por ejemplo,  15 - 1 * ( 5 *( 1 + 2 ) ) = 0.

8. Los operadores de exponenciación utilizan enlazado del lado derecho, por ejemplo, 2 ** 2 ** 3 = 256.
"""
# Cuestionario

print((2**4), (2 * 4.0), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2**3**2))

# Variables
# Variables cajas con forma de datos
"""
Pero es normal preguntar como es que se pueden almacenar los resultados de estas operaciones, para poder emplearlos en otras operaciones, y así sucesivamente.

¿Cómo almacenar los resultados intermedios, y después utilizarlos de nuevo para producir resultados subsecuentes?

Python ayudará con ello. Python ofrece "cajas" (o "contenedores") especiales para este propósito, estas cajas son llamadas variables ‒ el nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.

¿Cuáles son los componentes o elementos de una variable en Python?

Un nombre;
Un valor (el contenido del contenedor)
Comencemos con lo relacionado al nombre de la variable.

Las variables no aparecen en un programa automáticamente. Como desarrollador, tu debes decidir cuantas variables deseas utilizar en tu programa.

También las debes de nombrar.
"""
# Nombres de las Variables
"""
Si se desea nombrar una variable, se deben seguir las siguientes reglas:

-El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo)
-El nombre de la variable debe comenzar con una letra;
-El carácter guion bajo es considerado una letra;
-Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el mundo real - Alicia y ALICIA 
son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes);
-El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python 
(las palabras clave - explicará más de esto pronto).

Nota que la misma restricción aplica a los nombres de funciones.

Python no impone restricciones en la longitud de los nombres de las variables, 
pero eso no significa que un nombre de variable largo sea mejor que uno corto.

Aquí se muestran algunos nombres de variable que son correctos, pero que no siempre son convenientes:

MyVariable
i
l
t34
Exchange_Rate
counter
days_to_christmas
TheNameIsTooLongAndHardlyReadable
_
Estos nombres de variables también son correctos:

Adiós_Señora
sûr_la_mer
Einbahnstraße
переменная.
Python te permite usar no solo letras latinas sino también caracteres específicos de idiomas que usan otros alfabetos.

Ahora veamos algunos nombres incorrectos:

10t (no comienza con una letra)
!important (no comienza con una letra)
exchange rate (contiene un espacio).

-Los nombres de las variables deben estar en minúsculas, 
con palabras separadas por guiones bajos para mejorar la legibilidad (por ejemplo, var, my_variable)
-Los nombres de las funciones siguen la misma convención que los nombres de las variables (por ejemplo, fun, my_function)
-También es posible usar letras mixtas (por ejemplo, myVariable), 
pero solo en contextos donde ese ya es el estilo predominante, 
para mantener la compatibilidad retroactiva con la convención adoptada.

Palabras Clave
Observa las palabras que juegan un papel muy importante en cada programa de Python.

['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Son llamadas palabras clave o (mejor dicho) palabras clave reservadas. 
Son reservadas porque no se deben utilizar como nombres: ni para variables, 
ni para funciones, ni para cualquier otra cosa que se desee crear.

El significado de la palabra reservada está predefinido, y no debe cambiar.

Afortunadamente, debido al hecho de que Python es sensible a mayúsculas y minúsculas, 
cualquiera de estas palabras se pueden modificar cambiando una o varias letras de mayúsculas a minúsculas o viceversa, 
creando una nueva palabra, la cual no esta reservada.

Por ejemplo - no se puede nombrar a la variable así:

import

No se puede tener una variable con ese nombre - esta prohibido. pero se puede hacer lo siguiente:

Import

Estas palabras podrían parecer un misterio ahorita, pero pronto se aprenderá acerca de su significado.
"""

# Como Crear Una Variable

"""
¿Qué se puede poner dentro de una variable?

Cualquier cosa.

Se puede utilizar una variable para almacenar cualquier tipo de los valores que ya se han mencionado, 
y muchos mas de los cuales aun no se han explicado.

El valor de la variable en lo que se ha puesto dentro de ella. 
Puede variar tanto como se necesite o requiera. El valor puede ser entero, después flotante, y eventualmente ser una cadena.

Hablemos de dos cosas importantes - como son creadas las variables, y como poner valores dentro de ellas (o mejor dicho, 
como dar o pasarles valores).

RECUERDA  
Una variable se crea cuando se le asigna un valor. A diferencia de otros lenguajes de programación, no es necesario declararla.

Si se le asigna cualquier valor a una variable no existente, la variable será automáticamente creada. 
No se necesita hacer algo más.

La creación (o su sintaxis) es muy simple: solo utiliza el nombre de la variable deseada, 
después el signo de igual (=) y el valor que se desea colocar dentro de la variable.

Observa el fragmento en el editor:
"""
var = 1
print(var)

# Como emplear una variable

var = 1
account_balance = 1000.0
client_name = "John Doe"
print(var, account_balance, client_name)
print(var)
"""Sin embargo, no se permite utilizar una variable que no exista, 
(en otras palabras, una variable a la cual no se le ha dado un valor).

Este ejemplo ocasionará un error:"""
# var = 1
# print(Var)

#  RECUERDA
"""Se puede utilizar 
print() para combinar texto con variables utilizando el operador + para mostrar cadenas con variables, por ejemplo:"""
var = "3.8.5"
print("Python version: " + var)

# Cómo asignar un nuevo valor a una variable ya existente
"""
¿Cómo se le asigna un valor nuevo a una variable que ya ha sido creada? De la misma manera. Solo se necesita el signo de igual.

El signo de igual es de hecho un operador de asignación. Aunque esto suene un poco extraño, el operador tiene una sintaxis simple y una interpretación clara y precisa.

Asigna el valor del argumento de la derecha al de la izquierda, aún cuando el argumento de la derecha sea una expresión arbitraria compleja que involucre literales, operadores y variables definidas anteriormente.

Observa el siguiente código:
"""
var = 1
print(var)
var = var + 1
print(var)

var = 100
var = 200 + 300
print(var)

# Resolviendo problemas matemáticos simples
"""
Ahora deberías poder construir un programa corto que resuelva problemas matemáticos simples como el teorema de Pitágoras:

El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos.

El siguiente código evalúa la longitud de la hipotenusa 
(es decir, el lado más largo de un triángulo rectángulo, el opuesto al ángulo recto)
usando el teorema de Pitágoras:
"""

a = 3.0
b = 4.0
c = (a**2 + b**2) ** 0.5
print("c =", c)

# LAB Variable
john = 3
mary = 5
adam = 6
print("John tiene:", john, "Mary tiene:", mary, "Adam tiene:", adam, sep=" ")
total_apples = john + mary + adam
print("total_apples: ", total_apples, "unids")

# Operadores Abreviados
"""Es tiempo de explicar el siguiente conjunto de operadores que harán la vida del programador/desarrollador más fácil. 
Muy seguido, se desea utilizar la misma variable al lado derecho y al lado izquierdo del operador = operator.

Por ejemplo, si se necesita calcular una serie de valores sucesivos de la potencia de 2, 
se puede usar el siguiente código:"""
x = 2
x = x * 2
print(x)

# También, puedes utilizar una expresión como la siguiente si no puedes dormir
# y estas tratando de resolverlo con alguno de los métodos tradicionales:
sheep = 1
sheep = sheep + 10
print(sheep)

# Python ofrece una manera más corta de escribir operaciones como estas,
# lo cual se puede codificar de la siguiente manera:

x *= 2
sheep += 1
print(x, sheep)

"""Observa los siguientes ejemplos. Asegúrate de entenderlos todos.

Expresión	Operador abreviado
i = i + 2 * j
i += 2 * j

var = var / 2
var /= 2

rem = rem % 10
rem %= 10

j = j - (i + var + rem)
j -= (i + var + rem)

x = x ** 2
x **= 2"""

# lab

kilometers = 12.25
miles = 7.38
miles_equal = 1.61 / 1
kilometers_equal = 1.61


miles_to_kilometers = miles * kilometers_equal
kilometers_to_miles = kilometers / miles_equal

print(miles, "millas son", round(miles_to_kilometers, 1), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 1), "millas")

# lab 2
x = 0
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = 1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

x = -1
x = float(x)
y = 3 * x**3 - 2 * x**2 + 3 * x - 1
print("y =", y)

"""
Una variable es una ubicación nombrada reservada para almacenar valores en la memoria. Una variable es creada 
o inicializada automáticamente cuando se le asigna un valor por primera vez. (2.1.4.1)

Cada variable debe de tener un nombre único - un identificador. Un nombre válido debe ser aquel que no contiene espacios,
debe comenzar con un guion bajo(_), o una letra, y no puede ser una palabra reservada de Python. El primer carácter puede estar seguido de guiones bajos, letras, y dígitos. Las variables en Python son sensibles a mayúsculas y minúsculas.

Python es un lenguaje de tipo dinámico, lo que significa que no se necesita declarar variables en él. 
Para asignar valores a las variables, se utiliza simplemente el operador de asignación, es decir el signo de igual (=), por ejemplo, var = 1.

También es posible utilizar operadores de asignación compuesta (operadores abreviados) 
para modificar los valores asignados a las variables, por ejemplo: var += 1, o var /= 5 * 2.

Se les puede asignar valores nuevos a variables ya existentes utilizando el operador de asignación o un operador abreviado, 
por ejemplo:"""

var = 2
print(var)

var = 3
print(var)

var += 1
print(var)

"""Puedes combinar texto y variables usando el operador + y emplear la función print() para generar cadenas y variables, 
por ejemplo:"""

var = "007"
print("Agent " + var)


# Cuestionario
a = "1"
b = "1"
print(a + b)

a = 6
b = 3
a /= 2 * b
print(a)

# comentarios

# este programa calcula los segundos en cierto número de horas determinadas
# este programa fue escrito hace dos días

a = 2  # número de horas
seconds = 3600  # número de segundos en una hora

print("Horas: ", a)  # imprime el numero de horas
print(
    "Segundos en Horas: ", a * seconds
)  # se imprime el numero de segundos en determinado numero de horas

print(
    "Adios"
)  # aquí también se debe de imprimir un "Adiós", pero el programador no tuvo tiempo de escribirlo
# este el es fin del programa que calcula el numero de segundos en 2 horas

# Resumen de comentarios
"""
Los comentarios pueden ser utilizados para colocar información adicional en el código. Son omitidos al momento de la ejecución.
Dicha información es para los lectores que están manipulando el código. En Python, 
un comentario es un fragmento de texto que comienza con un #. El comentario se extiende hasta el final de la línea.

Si deseas colocar un comentario que abarque varias líneas, es necesario colocar un # al inicio de cada línea. Además, 
se puede utilizar un comentario para marcar un fragmento de código que no es necesario en el momento y no se desea ejecutar. 
(observa la última línea de código del siguiente fragmento), por ejemplo:"""

# Este programa imprime
# una introducción en la pantalla.
print("¡Hola!")  # Invocando a la función print()
# print("Soy Python.")

"""Cuando sea posible, se deben auto comentar los nombres de las variables, por ejemplo, 
si se están utilizando dos variables para almacenar la altura y longitud de algo, 
los nombres length y width son una mejor elección que myvar1 y myvar2.

Es importante utilizar los comentarios para que los programas sean más fáciles de entender, 
además de emplear variables legibles y significativas en el código. Sin embargo, 
es igualmente importante no utilizar nombres de variables que sean confusos, 
o dejar comentarios que contengan información incorrecta.

Los comentarios pueden ser muy útiles cuando tú estás leyendo tu propio código después de un tiempo 
(es común que los desarrolladores olviden lo que su propio código hace), 
y cuando otros están leyendo tu código (les puede ayudar a comprender que es lo que hacen tus programas y como es que lo hacen).
"""

# print(1/1)

# x = 1 / 2 + 3 // 3 + 4 ** 2
# print(x)

# z = y = x = 1
# print(x, y, z, sep='*')

# x = int(input())
# y = int(input())

# x = x / y
# y = y / x

# print(y)


# x = input()
# y = int(input())

# print(x * y)

# x = int(input())
# y = int(input())

# x = x % y
# x = x % y
# y = y % x

# print(y)


# x = int(input())
# y = int(input())

# print(x+y)

# x = int(input())
# y = int(input())

# x = x // y
# y = y // x

# print(y)

# x = input()
# y = input()
# print(x + y)

x = 1
y = 2
z = x
x = y
y = z
print(x, y)

print(1 // 2 * 3)
