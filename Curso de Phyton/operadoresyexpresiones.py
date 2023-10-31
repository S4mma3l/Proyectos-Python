print("Hola como estas! Por favor indica la Hora, Minutos y duracion de tu Curso")
hora = int(input("Hora de inicio de tu curso: "))
minutos = int(input("Minutos: "))
duracion = int(input("Duracion de tu Curso: "))

hora_entrada = hora
minutos_entrada = minutos
duracion_curso = duracion

duracion_hora = 60
horas_dia = 24

minutos = minutos + duracion
hora = hora + minutos // duracion_hora
minutos = minutos % duracion_hora
hora = hora % horas_dia

print(
    "Tu curso inicia a las: ",
    hora_entrada,
    ":",
    minutos_entrada,
    "y dura: ",
    duracion_curso,
    "Minutos",
    "Saldras a la siguiente hora: ",
    hora,
    ":",
    minutos,
    sep=" ",
)

# Resumen
"""
1.La función print() envía datos a la consola, mientras que la función input() obtiene datos de la consola.

2. La función input() viene con un parámetro opcional: la cadena de mensaje. 
Te permite escribir un mensaje antes de que el usuario ingrese algo, por ejemplo:

name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". ¡Un gusto conocerte!")
 
3. Cuando la función input() es llamada o invocada, el flujo del programa se detiene, el símbolo del cursor se mantiene parpadeando (le está indicando al usuario que tome acción ya que la consola está en modo de entrada) hasta que el usuario haya ingresado un dato y/o haya presionado la tecla Enter.

NOTA  
Puedes probar la funcionalidad completa de la función input() localmente en tu máquina. Por razones de optimización, se ha limitado el máximo número de ejecuciones en Edube a solo algunos segundos únicamente. Ve a Sandbox, copia-pega el código que está arriba, ejecuta el programa, y espera unos segundos. Tu programa debe detenerse después de unos segundos. Ahora abre IDLE, y ejecuta el mismo programa ahí -¿Puedes notar alguna diferencia?

Tip: la característica mencionada anteriormente de la función input() puede ser utilizada para pedirle al usuario que termine o finalice el programa. Observa el siguiente código:


name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". '¡Gusto en conocerte'!")
 
print("\nPresiona Enter para terminar el programa.")
input()
print("FIN.")
 
4. El resultado de la función input() es una cadena. Se pueden unir cadenas unas con otras a través del operador de concatenación (+). Observa el siguiente código:


num_1 = input("Ingresa el primer número: ") # Ingresa 12
num_2 = input("Ingresa el segundo número: ") # Ingresa 21
 
print(num_1 + num_2) # El programa retorna 1221
 
5. También se pueden multiplicar (* - replicación) cadenas, por ejemplo:


my_input = input("Ingresa algo: ") # Entrada de ejemplo: hola
print(my_input * 3) # Salida Esperada: holahola
 
"""
