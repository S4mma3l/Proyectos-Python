import pathlib
import time
import subprocess
from timeit import timeit

def concatenar(ruta,i,j):
    ruta = str(pathlib.Path(ruta))
    lista = [ruta,'/', str(i),'/', str(i), '.', str(j)]
    ruta_nueva = ''.join(lista)
    return ruta_nueva #retornamos la ruta


ruta = pathlib.Path("C:/Users/azaze/Documents/ ").parent.absolute() # Obtiene el directorio actual
carpetas = int(input("Ingrese el número de carpetas: "))
subcarpetas = int(input("Ingrese el número de subcarpetas: "))

for i in range(1, carpetas + 1):
    archivo = str(pathlib.Path(ruta))
    fullpath = pathlib.Path(archivo + '/' + str(i)).mkdir()
    for j in range(1, subcarpetas + 1):
        pathlib.Path(concatenar(ruta,i,j)).mkdir()


'''
program = subprocess.run(["C:\Program Files\Autodesk\Inventor 2023\Bin\Inventor.exe"], capture_output=True, text=True)
#program_2 = subprocess.run(["C:\Program Files\Adobe\Adobe Illustrator 2023\Support Files\Contents\Windows\Illustrator.exe"])
#program_3 = subprocess.run(["C:\Program Files\Adobe\Adobe Photoshop 2023\Photoshop.exe"])

# def control_tiempo(I_T, T_F, T_T):
    
#     I_T = time.time()
#     T_F = time.time() 
#     T_T = T_F - I_T
#     print ("\nTomo %d segundos." % (T_T))


if program.returncode == 0: 
  print(f'El programa "{program}" está instalado')

  print(f'La ubicación del binario es: {program.stdout}')
else:
  print(f'Lo sentimos el {program} no está instalado')

  print(program.stderr)
 
  print (program.stdout)
    
'''
