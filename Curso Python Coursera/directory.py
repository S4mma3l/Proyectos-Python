'''
ver el directorio activo en python os.getcdw()
algo pwd en linux
'''
import os

print(os.getcwd())

# os.mkdir("new_dir") # crea una nueva carpeta
os.chdir("new_dir") # ingresar a directorios
# os.rmdir() nos permite eliminar carpetas vacias
os.listdir() #nos permite listar los archivos en una carpeta

#  la funcion join en os.path.join nos permite un string que funcione en todas las plataformas y concatenar los directorios