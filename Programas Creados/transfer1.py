import shutil
import os

print(os.getcwd()) # Mostrar la ubicacion de mi archivo

# Path original del directorio
orig_path = input("\n""Ingrese la ruta donde se encuentra los archivos a copiar: ")
orig_path_name = orig_path.replace("\\", "/") # remplazo simbolos
    
# Nuevo path del directorio
print("\n""Para ingresar una ruta la puedes copiar desde el explorador")

new_path = input("\n""Ingrese la ruta # 1 donde va a copiar los archivos: ")
new_path_name = new_path.replace("\\", "/") # remplazo simbolos

# Mover directorio
shutil.copytree(orig_path, new_path_name) # Mover los archivos de un directorio a otro

ruta_0 = os.chdir(new_path_name)

i = 1
for file in os.listdir(ruta_0):
    new_file_name = "1_{}.ipt".format(i)
    os.rename(file, new_file_name)
    
    i = i + 1
   
print("\n"f"Se copiaron los archivos con exito en la ruta {new_path_name}""\n")
archivos = os.listdir(new_path_name)
print (archivos)
print("\n""Programa Desarrollador por S4mma3l")
print("Visitame en https://github.com/S4mma3l")