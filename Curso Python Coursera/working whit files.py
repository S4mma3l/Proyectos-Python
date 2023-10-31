import os

# os. remove ("novel.txt") # eliminar archivos

# os.rename ("firts_draft.txt", "finished_masterpiece.txt") #renombrar una archivo

os.path.exists("finished_masterpiece.txt")

os.path.exists("guests.txt")

os.path.exists("userlist.txt")  # ver si existe un archivo

os.path.getsize("guests.txt")  # tamano de un archivo

os.path.getmtime("guests.txt")  # ver cuando se modifico
# brindara un numero (timestamp)que es la una marca de tiempo
# de unix representa el nuemro de segundos desde 1 de enero de 1970
# se puede usar el modulo datetime para ser entendible

import datetime

timestamp = os.path.getmtime("guests.txt")
datetime.datetime.fromtimestamp(timestamp)

'''import os

file = "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))  # Prueba de modulo
else:
    print(os.path.isfile(file))
print("File not found")


# funcion abspath me indica la ruta del archivo

os.path.abspath("guests.txt")'''
