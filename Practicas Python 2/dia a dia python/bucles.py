# while loops
x = 0
while x < 5:
    print("not there yet, x =" + str(x))
    x = x + 1
print("x = " + str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(5)


"""
username = get_username()
while not valid_username(username):
    print("invalid username")
    username = get_username()
"""
# Errores comunes en una variable
"""while my_variable < 10:
    print("Hello")          # Error
    my_variable +=1"""

my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1


def count_down(start_number):
    current = 3  # variable faltante
    while current > 0:
        print(current)
        current -= 1
    print("Zero!")


count_down(3)

# Infinite loops and how to break them

"""def print_range(start, end):
	n = start
	while n <= end:
		print(n)
    
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line) 
"""

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

# This while loop prints the multiples of 5 between 1 and 50. The
# "multiplier" variable is initialized with the starting value of 1.
# The "result" variable is initialized with the value of the
# "multiplier" variable times 5.

# The while loop specifies that the loop must iterate while it is True
# that the "result" is less than or equal to 50. Within the while loop,
# the code tells the Python interpreter to print the value of the
# "result" variable. Then, the "multiplier" is incremented by 1 and the
# "result" is assigned the new value of the "multiplier" times 5.

# The end of the while loop is indicated by the indentation of the next
# line of code moving one tab to the left. At this point, the Python
# interpreter automatically loops back to the beginning of the while
# loop to check the condition again with the new value of the "result"
# variable. When the while loop condition becomes False (meaning
# "result" is no longer less than or equal to 50), the interpreter exits
# the loop and reads the next line of code outside of the loop. In this
# case, that next line tells the interpreter to print the string "Done".

# Click the "Run" button to check the result of this while loop.

# This function outputs an addition table. It is written to end after
# printing 5 lines of the addition table, but it will break out of the
# loop if the "my_sum" variable exceeds 20.


# The function accepts a "given_number" variable through its
# parameters.
def addition_table(given_number):
    # The "iterated_number" and "my_sum" variables are initialized with
    # the value of 1. Although the "my_sum" variable does not need any
    # specific initial value, it still must be assigned a data type
    # before being used in the while loop. By initializing "my_sum"
    # with any integer, the data type will be set to int.
    iterated_number = 1
    my_sum = 1

    # The while loop will run while it is True that the
    # "iterated_number" is less than or equal to 5.
    while iterated_number <= 5:
        # The "my_sum" variable is assigned the value of the
        # "given_number" plus the "iterated_number" variables.
        my_sum = given_number + iterated_number

        # Test to see if the "my_sum" variable is greater than 20.
        if my_sum > 20:
            # If True, then use the break keyword to exit the loop.
            break
        # If False, the Python interpreter will move to the next line
        # in the while loop after the if-statement has ended.

        # The print function will output the "given_number" plus
        # the "iterated_number" equals "my_sum".
        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

        # Increment the "iterated_number" before the while loop starts
        # over again to print a new "my_sum" value.
        iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)

# Expected output:
# 5 + 1 = 6
# 5 + 2 = 7
# 5 + 3 = 8
# 5 + 4 = 9
# 5 + 5 = 10
# 17 + 1 = 18
# 17 + 2 = 19
# 17 + 3 = 20
# None


# This function counts the number of integer factors for a
# "given_number" variable, passed through the function’s parameters.
# The "count" return value includes the "given_number" itself as a
# factor (n*1).
def count_factors(given_number):
    # To include the "given_number" variable as a "factor", initialize
    # the "factor" variable with the value 1 (if the "factor" variable
    # were to start at 2, the "given_number" itself would be excluded).
    factor = 1
    count = 1

    # This "if" block will run if the "given_number" equals 0.
    if given_number == 0:
        # If True, the return value will be 0 factors.
        return 0

    # The while loop will run while the "factor" is still less than
    # the "given_number" variable.
    while factor < given_number:
        # This "if" block checks if the "given_number" can be divided by
        # the "factor" variable without leaving a remainder. The modulo
        # operator % is used to test for a remainder.
        if given_number % factor == 0:
            # If True, then the "factor" variable is added to the count of
            # the "given_number"’s integer factors.
            count += 1
        # When exiting the if block, increment the "factor" variable by 1
        # to divide the "given_number" variable by a new "factor" value
        # inside the while loop.
        factor += 1

    # When the interpreter exits either the while loop or the top if
    # block, it will return the value of the "count" variable.
    return count


print(count_factors(0))  # Count value will be 0
print(count_factors(3))  # Should count 2 factors (1x3)
print(count_factors(10))  # Should count 4 factors (1x10, 2x5)
print(count_factors(24))  # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6).


def is_power_of_two(number):
    # This while loop checks if the "number" can be divided by two
    # without leaving a remainder. How can you change the while loop to
    # avoid a Python ZeroDivisionError?
    if number == 0:
        return False
    while number % 2 == 0:
        number = number / 2
    # If after dividing by 2 "number" equals 1, then "number" is a power
    # of 2.
    if number == 1:
        return True
    return False


# Calls to the function
print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

# Fill in the blanks so that the while loop continues to run while the
# "divisor" variable is less than the "number" parameter.


def sum_divisors(number):
    divisor = 1
    total = 0

    if number < 1:
        return 0
    while divisor < number:
        if number % divisor == 0:
            total += divisor
        divisor += 1
    return total


print(sum_divisors(0))
print(sum_divisors(3))
print(sum_divisors(36))
print(sum_divisors(102))


def multiplication_table(number):
    multiplier = 1

    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        multiplier += 1


multiplication_table(3)


multiplication_table(5)


multiplication_table(8)

# for loop

"""y = int(input("ingresa un numero: "))
for x in range(5):
   y += 1
   print(y)"""

friends = ["Taylor", "Alex", "Pat", "Eli"]
for friend in friends:
    print("Hola " + friend)

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1
print("total sum: " + str(sum) + " - average: " + str(sum / length))

print(23 + 52 + 59 + 37 + 48)

product = 1
for n in range(1, 10):
    product = product * n
print(product)


def to_celsius(x):
    return (x - 32) * 5 / 9


for x in range(0, 101, 10):
    print(x, to_celsius(x))

"""
range(stop)

    range(3) 

    range(3+1) 

range(start, stop)

    range(2, 6)     

    range(5,10+1) 

range(start, stop, step)

    range(4, 15+1, 2)         

    range(2*2, 25, 3+2) 

    range(10, 0, -2)  
"""
"""
Una mirada más cercana a la función Range()

La palabra clave in, cuando se usa con la función range(), genera una secuencia de números enteros, que se puede usar con un ciclo for para controlar 
el punto de inicio, el punto final y los valores incrementales del ciclo.

Sintaxis:
for n in range(x, y, z):
    print(n)


La función range() utiliza un conjunto de índices que apuntan a valores enteros, que comienzan en el número 0. 
Los valores numéricos 0, 1, 2, 3, 4 se correlacionan con las posiciones de índice ordinal 1, 2, 3, 4 y 5. Entonces,
cuando se realiza una llamada de rango a la quinta posición del índice usando range(5), el índice apunta al valor numérico de 4.
Index Number	1st index	2nd index	3rd index	4th index	5th index
Value	            0	         1	        2	       3	        4


La función range() puede tomar hasta tres parámetros: range(start, stop, step)

Comenzar
El primer elemento en los parámetros de la función range() es la posición inicial del rango. El valor predeterminado es la primera posición del índice, 
que apunta al valor numérico 0. Este valor se incluye en el rango.

Detener
El segundo elemento en los parámetros de la función range() es la posición final del rango. No hay una posición de índice predeterminada, 
por lo que este número de índice debe asignarse a los parámetros range(). Por ejemplo, 
la línea para n en range(4) se repetirá 4 veces con la variable n comenzando en 0 y recorriendo 4 posiciones de índice: 0, 1, 2, 3. Como puede ver, 
range(4) (que significa posición de índice 4) termina en el valor numérico 3. En Python, 
esta estructura se puede expresar como "el valor de fin de rango se excluye del rango". Para incluir el valor 4 en range(4), 
la sintaxis se puede escribir como range(4+1) o range(5). Ambos rangos producirán los valores numéricos 0, 1, 2, 3, 4.

Paso
El tercer elemento en los parámetros de la función range() es el valor del paso incremental. 
El incremento predeterminado es +1. El valor predeterminado se puede anular con cualquier incremento válido. Sin embargo, 
tenga en cuenta que el bucle terminará en la posición de índice de fin de rango, independientemente del valor incremental. 
Por ejemplo, si tiene un ciclo con el rango: para n en el rango (1, 5, 6), el rango solo producirá el valor numérico 1. 
Esto se debe a que el valor incremental de 6 excedió el punto final del rango.

Ejercicio práctico

Puede usar el bloque de código a continuación para probar los valores de n con varios parámetros range(). Algunas sugerencias para probar son:

rango (detener)

     rango(3)

     rango (3+1)

rango (inicio, parada)

     rango (2, 6)

     rango (5,10+1)

rango (inicio, parada, paso)

     rango (4, 15+1, 2)

     rango (2*2, 25, 3+2)

     rango (10, 0, -2)

  
1
2

  
Ejemplos de la función range() en código:
  
Conclusiones clave

Los roles de los parámetros de la función range(start, stop, step) son:

     Inicio - Comienzo del rango

         valor incluido en el rango

         predeterminado = 0

     Parada - Fin de rango

         valor excluido del rango (para incluir, use stop+1)

         ningún valor predeterminado

         debe proporcionar el número de índice final

     Paso - Valor incremental

         predeterminado = 1

"""
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
print()

teams = ["Dragons", "Wolves", "Pandas", "Unicors"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# case base

def factorial(n):
    if n < 2: #bloque condicional llamado Base case
        return 1
    return n * factorial(n - 1) # este bloque es un recursive case
print(factorial)# la funcion recursiva no debe de exceder los 1000 niveles

def factorial(n):
    print("Factorial called with" + str(n))
    if n < 2:
        print(" Returning 1 ")
        return 1
    result = n * factorial(n-1)
    print(" Returning " + str(result) + " for factorial of " + str(n))
    return result
factorial(4)

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

''' estructura de una formula recursiva
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
'''

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  number = number / base
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return False
  else:
      return True

  # Recursive case: keep dividing number by base.
  return is_power_of(number, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


'''def count_users(group):
  count = 0
  for member in get_members(group):
    #count += 1
    if is_group(member):
      count += count_users(member)
    else:
        count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18'''

def sum_positive_numbers(n):
  if n < 1:
      return 0
  return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

#  para que se usa la recursividad: La recursividad se usa para llamar a una función desde dentro de la misma función.

# Loop Wrap Up

#esto es un while loop
x = 1
sum = 0
while x < 10:
    sum += x
    x += 1
product = 1
while x < 10:
    product = product * x
    x += 1
print( sum, product)

# esto es un bucle for
for x in range(5):
    print(x)

# esto es un bucle recursivo

def factorial(n):
    print("Factorial called with" + str(n))
    if n < 2:
        print(" Returning 1 ")
        return 1
    result = n * factorial(n-1)
    print(" Returning " + str(result) + " for factorial of " + str(n))
    return result
factorial(4)

# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
def count_by_10(end):
    # Initializeq the "count" variable as a string.
    count = ""

    # The range function parameters instruct Python to start the count  
    # at 0 and stop at the variable given as the upper end of the range. 
    # Since the value of the high end of a range is excluded by default,  
    # you can make Python include the "end" value by adding +1 to it. 
    # The third parameter tells Python to increment the count by 10.
    for number in range(0,end+1,10):

        # Although the variable "count" will hold a count of integers,  
        # this example will be converted to a string using "str(number)" 
        # in order to display the incremental count from 0 to the "end" 
        # value on the same line with a space " " separating each 
        # number.  
        count += str(number) + " "
        
    # The .strip() method will trim the final space " " from the end of 
    # the string "count"  
    return count.strip()


# Call the function with 1 integer parameter.
print(count_by_10(100))
# Should print 0 10 20 30 40 50 60 70 80 90 100

# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names. 
    n1 = initial_number 
    n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the columns.
    for column in range(n1, n2):

        # The nested for loop will create the rows.
        for row in range(n1, n2):

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the 
            # end of the row. You can override the default behavior of the 
            # print() function (which inserts a new line character after 
            # the print command runs) by using the "end=" "" parameter 
            # inside the print() function.  
              print(column*row, end=" ")

        # The row ends when the upper range value is encountered within the 
        # nested for loop. The outer (column) for loop should insert a new line
        # to create the next row. Use the print() function new line default 
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters. 
matrix(1, 4)
# Should print:
# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16 

# For this example, the outer for loop uses an end of range index of 
# 10. The value of index 10 will be 10-1, or 9.  
for outer_loop in range(10):

    # Using the "outer_loop" variable as the end of range for the  
    # inner loop, means the end of range index will be 9. The value 
    # of index 9 will be 9-1, or 8.
    for inner_loop in range(outer_loop):

        # The printed result is the value of "inner_loop". Since  
        # there aren’t any calculations in this loop, there is a 
        # simple shortcut for solving what the final value printed 
        # by the "inner_loop" will be. The solution is to simply use 
        # the value of the "inner_loop" index, which is 8.
        print(inner_loop)

'''
Encuentre y corrija un error en un bucle for con la función range().
'''
# This function should count down by -2 from 11 to 1, so that it only
# prints odd numbers. 

# This range(11, -2) tells the for loop to start at 11 and end at index
# position -2 (which corresponds to the numeric value of -1). Since the
# third incremental or decremental value is missing, the loop will 
# increment by the default of +1 instead of the intended -2 decrement.
# Starting at index position 11 and incrementing by +1 will end the loop 
# automatically, because the index is not counting down towards -2 as 
# the end of the range. 

# To fix this problem, the range() needs three parameters:
# First parameter should be the starting index position of 11.
# Second parameter should be the ending index position of 0 (value 1).
# Third parameter should be decrementing by -2.
# So, the range should be configured as range(11, 0, -2).

# Fix this loop with the corrected range parameters and click Run.
for n in range(11, -2):
    if n % 2 != 0:
        print(n, end=" ")

# Should print: 11, 9, 7, 5, 3, 1 once the problem is fixed.

'''
    Use a while loop to print a sequence of numbers .
'''

# For this example, the while loop will count down by threes starting 
# from 18 and ending at 0.
starting_number = 18

# The while loop will continue to loop until it reaches 0.
while starting_number >= 0:

    # To make the sequence of numbers easier to read, include a space
    # between each number in the sequence. You can override the default 
    # behavior of the print() function by using the "end=" parameter with
    # the print() function. The syntax for adding a space is: end=" " 
    print(starting_number, end=" ")
    
    # Decrement the "starting_number" variable by -3.
    starting_number -= 3

# Should print 18 15 12 9 6 3 0 



'''
Use un ciclo while para contar el número de dígitos en un valor numérico
'''


# It counts the number of digits in the salary and 
# returns the sentence like:
# "The CEO has a 6-figure salary."
def X_figure(salary):
    
    # Initializes the counter as an integer.
    tally = 0

    # The if-statement checks if the variable "salary" 
    # is equal to 0.
    if salary == 0:
        # If true, then it increments the counter to 
        # show there is 1 digit in 0.
        tally += 1

    # The while loop starts to run while the "salary"
    # is greater than or equal to 1 (the loop will 
    # not run if the "salary" is 0).
    while salary >= 1:

        # The body of the while loop counts the digits 
        # in "salary" by counting the number of times 
        # "salary" can be divided by 10 until "salary" 
        # is no longer >= 1.
        salary = salary/10

        # Add 1 to the counter to tally the number of 
        # times the loop runs.
        tally += 1

    # Return the results of the "tally" of the number
    # of digits in "salary".
    return tally
 
# Call the X_figure function with 1 parameter, converted to a string,
# inside a print function with additional strings.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")

# Should print"The CEO has a 7-figure salary."

'''
Habilidad 3: Uso de bucles while con sentencias if-else

     Utilice una función para aceptar dos enteros variables.

     Use sentencias if-else anidadas y bucles while para contar hacia adelante o hacia atrás desde la primera variable hasta la segunda variable.
'''


# This function will accept two integer variables: the floor
# number that a passenger "enter"s an elevator and the floor
# number the passenger is going to "exit". Then, the function
# counts up or down from the two floor numbers.
def elevator_floor(enter, exit):
    # The "floor" variable will be used as a counter and to  
    # print the floor numbers. The "elevator_direction"
    # variable will hold the string "Going up: " or 
    # "Going down: " plus the count up or down of the 
    # "floor" numbers.
    floor = enter
    elevator_direction = ""

    # If the passenger enters the elevator on a floor that  
    # is higher than the destination floor:
    if enter > exit:
        
        # Then the "elevator_direction" string will be 
        # initialized with the string "Going down: ".
        elevator_direction = "Going down: "

        # While the "floor" number is greater than or  
        # equal to the exit floor number:
        while floor >= exit:
            # The "floor" number is converted to a string 
            # and is appended to the string variable 
            # "elevator_direction".
            elevator_direction += str(floor)

            # If the "floor" number is still greater than  
            # the exit floor number:
            if floor > exit:

                # A pipe | character is added between each  
                # floor number in the string variable  
                # "elevator_direction" to provide a visual  
                # divider between numbers. The if-statement 
                # above (if floor > exit) prevents the pipe 
                # character from appearing after the "floor" 
                # number is no longer greater than the "exit" 
                # variable. 
                elevator_direction += " | "
                
                # Decrement the "floor" number as the elevator 
                # goes down.
            floor -= 1

    # Else, it is implied that the passenger is entering the  
    # elevator on a floor that is lower than the destination 
    # floor.
    else:

        # The "elevator_direction" string will be initialized 
        # with the string "Going up: ".
        elevator_direction = "Going up: "
        
        # While the "floor" number is less than or equal to the 
        # "exit" floor number:
        while floor <= exit:

            # Convert the the "floor" number to a string and append 
            # it to the string variable "elevator_direction".
            elevator_direction += str(floor)

            # If the entry floor number is still less than the exit 
            # floor number:
            if floor < exit:

                # The pipe | character is added between each  
                # floor number in the string variable  
                # "elevator_direction" to provide a visual  
                # divider between numbers. The if-statement 
                # above (if floor < exit) prevents the pipe 
                # character from appearing after the "floor" 
                # number is no longer less than the "exit" 
                # variable. 
                elevator_direction += " | "

            # Increments the "floor" number as the elevator goes up.
            floor += 1

    # Returns the string holding the elevator direction (Going down or 
    # Going up) along with the floor countdown or count up.
    return elevator_direction


# Call the function with 2 integer parameters. 
print(elevator_floor(1,4)) # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6,2)) # Should print Going down: 6 | 5 | 4 | 3 | 2

'''
Recordatorio: la sintaxis correcta es crítica

El uso de una sintaxis precisa es fundamental al escribir código en cualquier lenguaje de programación, incluido Python. Incluso un pequeño error tipográfico puede causar un error de sintaxis y el calificador de prueba automatizado codificado en Python marcará su código como incorrecto. Esto refleja errores de codificación de la vida real en el sentido de que un solo error de ortografía, mayúsculas y minúsculas, etc. puede hacer que su código falle. Los problemas de codificación causados por una sintaxis imprecisa siempre serán un problema, ya sea que esté aprendiendo un lenguaje de programación o esté usando habilidades de programación en el trabajo. Por lo tanto, es fundamental comenzar ahora el hábito de ser preciso en su código.

No se otorgará crédito si hay errores de codificación en los cuestionarios calificados automatizados, incluidos errores menores. Afortunadamente, tiene 3 oportunidades opcionales para volver a tomar las pruebas calificadas en este curso. Además, tiene repeticiones ilimitadas de cuestionarios de práctica y puede revisar los videos y las lecturas tantas veces como necesite para dominar los conceptos de este curso.

Ahora, antes de comenzar el cuestionario calificado, revise esta lista de errores de sintaxis comunes que cometen los codificadores al escribir código.
Errores comunes de sintaxis:

     faltas de ortografía

     sangrías incorrectas

     Caracteres clave faltantes o incorrectos:

         Tipos entre paréntesis - ( curvo ), [ cuadrado ], { rizado }

         Tipos de cotización: "recta-doble" o 'recta-simple', "curly-doble" o 'curly-single'

         Bloquee los caracteres de introducción, como los dos puntos:

     Discrepancias en el tipo de datos

     Palabras reservadas de Python que faltan, se usan incorrectamente o se extravían

     Usar el caso incorrecto (mayúsculas/minúsculas): Python es un lenguaje que distingue entre mayúsculas y minúsculas
'''
