import shutil
import os
from tkinter import ttk
from tkinter import *


class move:
    def __init__(self, window):
        self.win = window
        self.win.title("App-Tranfer")

        frame = LabelFrame(self.win, text="Transfer-Data")
        frame.grid(row=0, column=0, columnspan=100, pady=20)

        Label(frame, text="Ruta 1: ").grid(row=1, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=1, column=1, columnspan= 7)
        frame.grid(row= 1, columnspan=7)

        Label(frame, text="Ruta 2: ").grid(row=2, column=0)
        self.name = Entry(frame)
        self.name.focus()
        self.name.grid(row=2, column=1, columnspan= 7)

        ttk.Button(frame, text="Ingrese la Ruta").grid(row=3, column=2, sticky=W + E)

        self.tree = ttk.Treeview(height=10, columns=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading("#0", text="Ruta", anchor=CENTER)
        self.tree.heading("#1", text="Ruta", anchor=CENTER)


if __name__ == "__main__":
    window = Tk()
    application = move(window)
    window.mainloop()
