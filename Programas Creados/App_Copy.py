import shutil
import os
from tkinter import ttk
from tkinter import *


class move:
    def __init__(self, window):
        self.win = window
        self.win.title("App-Tranfer")
        self.win.geometry("600x300")

        # marco total
        frame = LabelFrame(self.win, text="Transfer-Data", fg="brown")
        frame.grid(row=0, column=0, columnspan=100, pady=20)

        # etiqueta de las rutas
        Label(frame, text="Ruta Origen: ", fg="green").grid(row=1, column=0)
        self.orig_path = Entry(frame)
        self.orig_path.focus()
        self.orig_path.grid(row=1, column=1, columnspan=7)
        frame.grid(row=1, columnspan=7)

        # etiqueta de las rutas
        Label(frame, text="Ruta Destino: ", fg="red").grid(row=2, column=0)
        self.new_path = Entry(frame)
        self.new_path.focus()
        self.new_path.grid(row=2, column=1, columnspan=7)

        ttk.Button(frame, text="cambiar Simbolos de Ruta", command=self.convert).grid(
            row=3, column=2, sticky=W + E
        )
        # boton para ejecutar la operacion
        ttk.Button(frame, text="tranferir los datos", command=self.add_route).grid(
            row=4, column=2, sticky=W + E
        )

        # texto a imprimir con inforacion de ruta o falta de ruta
        self.message = Label(text="", fg="gray")
        self.message.grid(row=4, column=0, columnspan=2, sticky=W + E)

        # texto a imprimir con inforacion de ruta o falta de ruta
        self.message_2 = Label(text="", fg="blue")
        self.message_2.grid(row=5, column=0, columnspan=2, sticky=W + E)

        # informacion de la ruta donde se encuenta el programa
        self.message_os = Label(text=os.getcwd(), fg="orange")
        self.message_os.grid(row=6, column=0, columnspan=2, sticky=W + E)

        # informacion del creador
        self.information = Label(text="Programa Desarrollador por S4mma3l", fg="pink")
        self.information.grid(row=8, column=0, columnspan=2, sticky=W + E)

        # informacion de la pagfuna de github
        self.information_two = Label(
            text="Visitame en https://github.com/S4mma3l", fg="purple"
        )
        self.information_two.grid(row=8, column=0, columnspan=2, sticky=W + E)

    def convert(self):
        self.var = self.orig_path.get()
        self.var = str.replace(self.var, "\\", "/")

        self.var_2 = self.new_path.get()
        self.var_2 = str.replace(self.var_2, "\\", "/")

    def validation(self):
        return len(self.orig_path.get()) != 0 and len(self.new_path.get()) != 0

    def add_route(self):
        if self.validation():
            self.orig_path.get()
            self.new_path.get()
            self.message["text"] = "Ruta 1 Ingresada {} Exitosamente".format(
                self.orig_path.get()
            )
            self.message_2["text"] = "Ruta 2 Ingresada {} Exitosamente".format(
                self.new_path.get()
            )
            self.orig_path.delete(0, END)
            self.new_path.delete(0, END)
        else:
            self.message["text"] = "Debes de Ingresar una Ruta de Origen".format(
                self.orig_path.get()
            )
            self.message_2["text"] = "Debes de Ingresar una Ruta Destino".format(
                self.new_path.get()
            )

        shutil.copytree(self.var, self.var_2)

        self.ruta_0 = os.chdir(self.var_2)

        i = 1

        for file in os.listdir(self.ruta_0):
            self.new_file_name = "1_{}.ipt".format(i)
            os.rename(file, self.new_file_name)
            i = i + 1

            print(self.var)


if __name__ == "__main__":
    window = Tk()
    application = move(window)
    window.mainloop()
