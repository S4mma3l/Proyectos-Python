# Listas

mi_lista = list()  # forma 1 de hacer una lista
mi_otra_lista = []  # forma 2 de hacer una listas

print(len(mi_lista))

mi_lista = [36, 43, 67, 89, 90, 36, 40, 74]
print(len(mi_lista))

mi_otra_lista = [36, 183, "Angel", "Hernandez"]
print(type(mi_otra_lista))
print(len(mi_otra_lista))
print(mi_otra_lista)

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-3])
print(
    mi_otra_lista.count("Angel")
)  # el count en este caso es para ver cuantas veces se repite un valor
print(mi_lista.count(36))

(
    edad,
    altura,
    nombre,
    apellido,
) = mi_otra_lista  # se deben de asignar todos los elementos
print(edad)  # asi puedo asignar nombre a la lista

print(mi_lista + mi_otra_lista)

mi_otra_lista.append("Morales")  # agrega un elemento mas a la lista al final
print(mi_otra_lista)

mi_otra_lista.insert(
    3, "azul"
)  # agrega un elemento mas a la lista pero en la posicion que le indique
print(mi_otra_lista)

mi_otra_lista.remove("Morales")  # elimina el elemento que le indique
print(mi_otra_lista)

mi_lista.remove(36)  # elimina solo uno de los elementos si se repite en mi lista
print(mi_lista)

mi_lista.pop()  # elimina el ultimo elemento
print(mi_lista)

print(
    mi_lista.pop()
)  # al imprimir el pop me imprime el ultimo elemento aislado de la lista
print(mi_lista)

print(
    mi_lista.pop(2)
)  # tambien le puedo indicar a el pop el elemento que quiero separar de mi lista
print(mi_lista)

mi_elemento_pop = mi_lista.pop(
    1
)  # de esta forma imprimo solo el elemto que estoy aislando
print(mi_elemento_pop)
print(mi_lista)

del mi_lista[
    2
]  # de esta forma elimino un elemto defintivamente no lo guarda en ningun lugar
print(mi_lista)

mi_nueva_lista = mi_lista.copy()  # realiza una copia de la lista en otra variable

mi_lista.clear()  # con clear limpio o borro todo los elementos de mi lista
print(mi_lista)
print(mi_nueva_lista)

mi_nueva_lista.reverse()  # cambiamos el orde lo invertimos
print(mi_nueva_lista)

mi_nueva_lista.sort()  # ordena los numeros, o por nombre o como se desee ordenar
print(mi_nueva_lista)


mi_lista = "Hola, Angel"  # en este caso ahy que tener cuidado con el tipado de dato como aca ya se cambio a "str"
print(mi_lista)
print(type(mi_lista))
