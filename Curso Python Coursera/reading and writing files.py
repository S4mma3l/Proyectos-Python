guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

'''
'r' open for reading (default)

'w' open for writing, truncating the file first

'x' open for exclusive creation, failing if the file already exists

'a' open for writing, appending to the end of file if it exists

'b' binary mode

't' text mode (default)

'+' open for updating (reading and writing)

El modo predeterminado es 'r' (abierto para leer texto, sinónimo de 'rt'). Los modos 'w+' y 'w+b' abren y truncan el archivo. Los modos 'r+' y 'r+b'
abren el archivo sin truncamiento.

Como se mencionó en la Descripción general, Python distingue entre E/S binaria y de texto. Los archivos abiertos en modo binario (incluyendo 'b' en 
el argumento de modo) devuelven contenidos como objetos de bytes sin decodificación. En el modo de texto (el predeterminado, o cuando se incluye 't' en 
el argumento de modo), el contenido del archivo se devuelve como str, los bytes se decodificaron primero usando una codificación dependiente de la 
plataforma o usando la codificación especificada si se da.
'''

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))