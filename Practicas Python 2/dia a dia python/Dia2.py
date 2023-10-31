mi_salto_de_line = "este es un\nsalto de linea"
print(mi_salto_de_line)

mi_tab_string = "\testa es una tabulacion"
print(mi_tab_string)

mi_escape = "\\teste es un \\n escape"
print(mi_escape)
# Formateo

name, apellido, edad = "Angel", "hernandez", 36
print(
    "Mi Nombre es: {} {} y Mi edad es: {}".format(name, apellido, edad)
)  # para .format se realiza con {}
print(
    "Mi nombre es: %s %s y Mi Edad es: %s" % (name, apellido, edad)
)  # y se puede realizar de esta manera tambien.
print(
    f"Mi Nombre es: {name} {apellido} y Mi edad es: {edad}"
)  # inferencia de datos con f

# Desempaquetado de caracteres

nombre = "Angel"
a, b, c, d, e = nombre
print(a)
print(b)
print(c)
print(d)
print(e)

# Division

salto_caracteres = nombre[1:5]
print(salto_caracteres)

salto_caracteres = nombre[-3]
print(salto_caracteres)

salto_caracteres = nombre[0:5:2]
print(salto_caracteres)

#  Reverso

nombre_reverso = name[::-1]
print(nombre_reverso)

# funciones del sistema

print(nombre.capitalize())
print(nombre.upper())
print(nombre.count("a"))
print(nombre.isnumeric())
print("1".isnumeric())
print(nombre.lower())
print(nombre.upper().isupper())
print(nombre.startswith("An"))
