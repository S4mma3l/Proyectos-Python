from PIL import Image # python3 -m pip install Pillow

import os

Dir_1 = "/Users/azaze/Documents/move/Prueba/"
Dir_2 = "/Users/azaze/Documents/move/PDF/"
Dir_3 = "/Users/azaze/Documents/move/XLS/"
Dir_4 = "/Users/azaze/Documents/move/ISO/"


try:
    os.mkdir(Dir_1)
except OSError:
    print("La creacion de las carpeta %s fallo" % Dir_1)
else:
    print("Se crearon las Carpetas: %s exitosamente" % Dir_1)

downloadsFolder = "/Users/azaze/Downloads/"
jpg_folder = "/Users/azaze/Documents/move/Imagenes/"
pdf_Folder = "/Users/azaze/Documents/move/PDF/"
xls_Folder = "/Users/azaze/Documents/move/XLS/"
iso_Folder = "/Users/azaze/Documents/move/ISO/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".pdf"]:
            os.rename(downloadsFolder + filename, pdf_Folder + "move_" + filename)

        if extension in [".xlsx"]:
            os.rename(downloadsFolder + filename, xls_Folder + "move_" + filename)

        if extension in [".iso"]:
            os.rename(downloadsFolder + filename, iso_Folder + "move_" + filename)
        
        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(jpg_folder + "compressed_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)