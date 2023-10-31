#  Tuplas

my_tuple = tuple()
my_other_tuple = () #formas de definir una tupla, una tupla es un conjunto de valores

my_tuple = (36, 183, "Angel", "Hernandez", "Madre")
my_other_tuple = ( 1, 2 , 3)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])




print(my_tuple.count("Hernandez"))
print(my_tuple.index("Angel"))

# my_tuple[1] = 190 una tupla es inmutable no se puede  modificar (TypeError: 'tuple' object does not support item assignment)


print(my_tuple + my_other_tuple)
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)# puedo convertir archivos de formato como en este caso que te tupla pasa a lista.
print(type(my_tuple))

my_tuple[4] = "Morales" #ya en este momento puedo modificar valores internos porque es una lista.
my_tuple.insert(1, "Morado")
my_tuple = tuple(my_tuple)# y aca la vuelvo a pasar de lista  a tupla.

print(my_tuple)
print(type(my_tuple))

# del my_tuple[2] # no se pueden elimar archivos concretos al ser inmutables

del my_tuple #puedo eliminar la tupla completamente de esta forma
# print(my_tuple)# y aca ya la tupla no existiria (NameError: name 'my_tuple' is not defined)
