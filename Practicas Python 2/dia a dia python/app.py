import tkinter as tk

# from tkinter import *

app = tk.Tk()
app.geometry("800x300")  # Dimensiones de la ventana se utiliza .geometry(ancho X alto)
app.configure(background="#228B22")  # Darle color al fondo
tk.Wm.wm_title(app, "Calculo de Materiales")  # Colocar nombre a la nuestro programa


# funcione para agregar a un boton
def Saludar():
    print(
        "Hola como estas?"
    )  # se puede agregar por medio de una funcion o bien como lo vemos en la opcion del commmand


# Variables para agregar a una entrada
variable_uno = tk.StringVar(app)  # variable para la entrada(entry)
variable_dos = tk.StringVar(app)

#  Botones

tk.Button(  # Metodo para agregar un Botton
    app,
    text="Boton",  # nombre
    font=("Hack Nerd Font Mono", 14),  # Fuente
    bg="#F0FFFF",  # color de fondo
    fg="#8A2BE2",  # color del texto
    # command = Saludar
    command=lambda: print(
        "Hola, Como estas? " + variable_uno.get()
    ),  # lo podemos realizar de esta forma tambien
    # aca agragamos la variable_uno con un . get para que almacene la variable y me la imprima en consola
    relief="flat",
).pack(
    fill=tk.BOTH,  # metodo para hacer que un boton me aparezca en ventana
    expand=True,  # ajuste a justificacion del boton
)

#  label

tk.Label(  # Metodo para agregar un label
    app,
    text="Etiqueta",
    font=("Hack Nerd Font Mono", 14),
    bg="#A52A2A",
    fg="#7FFF00",
    justify="center",  # Esto jistifuca el texto a una zona del label
    # command = Saludar,
).pack(
    fill=tk.BOTH,  # metodo para hacer que un boton me aparezca en ventana
    expand=True,  # esto justifica el label en zona simetricas
)

# Entrada de texto

tk.Entry(  # Metodo para agregar una entrada de texto
    app,
    font=("Hack Nerd Font Mono", 14),
    bg="#556B2F",
    fg="#FFFACD",
    justify="center",  # Esto jistifuca el texto a una zona de la ventana
    textvariable=variable_uno,
).pack(
    fill=tk.BOTH,  # metodo para hacer que un boton me aparezca en ventana
    expand=True,  # esto justifica el label en zona simetricas
)


app.mainloop()
