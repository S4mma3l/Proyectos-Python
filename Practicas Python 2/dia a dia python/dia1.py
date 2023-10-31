# hola mundo

print("Hola, Mundo!!!")

"""
este es un comentario
"""

my_string = "Esto es una cadena de texto"
my_string = "cambio de valor del string"
print(type(my_string))
print(my_string)

my_string = 78
print(type(my_string))
print(my_string)

my_int = 72
my_int = my_int + 56
print(my_int)
print(my_int - 2)

my_float = 76.5
print(type(my_float))

my_bool = True
print(my_bool)
print(type(my_bool))

print(
    "el valor de mi entero es "
    + str(my_int)
    + " y el valor de mi booleano es "
    + str(my_bool)
    + "ademas mi valor flotante es "
    + str(my_float)
)  # convierto a string con str
print(
    f"el valor de mi entero es {my_int} y el valor de mi booleano es {my_bool} ademas mi valor flotante es {my_float}"
)  # interpolar una cadena se realiza con f

my_list = [my_string, my_int, my_bool, my_float]  # este se realisa entre [ ]
print(type(my_list))
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

mi_diccionario = {
    "string": my_string,
    "int": my_int,
    "bool": my_bool,
    "float": my_float,
    "sammael": "Angel HM",
}  # se debe de indicar nombre diferente a cada variable este se realiza entre{ }
print(type(mi_diccionario))
print(mi_diccionario)
print(mi_diccionario["float"])
print(mi_diccionario["sammael"])

my_set = {
    my_string,
    my_int,
    my_bool,
    my_float,
}  # esta es un set funciona para estructuras deordenadas y van entre { }
print(type(my_set))
print(my_set)

my_tuple = (
    my_string,
    my_int,
    my_bool,
    my_float,
)  # esto es una tupla funciona para estructuras ordenadas y va entre ( ) la diferencia con un diccionario es que es ordenada y se pueden repetir variables
print(type(my_tuple))
print(my_tuple)

if my_int == 11:
    print("en valor es: 11")
elif my_int == 128:
    print("el valor es 128 ")
else:
    print("el valor no es: 11")
for my_item in my_list:
    print(my_item)
for my_item in range(10):
    print(my_item)
for my_item in mi_diccionario:
    print(my_item)
for my_item in my_set:
    print(my_item)
for my_item in my_tuple:
    print(my_item)


def mi_funcion():  # esto es una funcion en python
    print("esto es una funcion")


for my_item in range(10):
    mi_funcion()


def mi_funcion_con_retorno():
    return 10


my_return = mi_funcion_con_retorno()
print(my_return)


class MyClass:
    def __init__(self, my_name):
        self.my_name = my_name

    def print_name(self):
        print(self.my_name)


my_class = MyClass("Hernandez")
my_class.print_name()
my_class.my_name = "Sammael"
print(type(my_class))
print(my_class.my_name)
