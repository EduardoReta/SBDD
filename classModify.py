import traceback
import tkinter as tk
from tkinter import messagebox
import re
from tkinter import *
from rich.console import Console
from rich import style
from datetime import datetime, timedelta, date
import time

class Modify:
    def __init__(self, master, cursor):
        self.master = master
        self.cursor = cursor
        self.frame = Frame(self.master)
        self.master.title("Add Window")
        self.master.geometry("600x600")

        self.book_button = Button(self.master, text="Libro")#, command=self.add_book_window)
        self.book_button.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.autor_button = Button(self.master, text="Autor")#, command=self.add_autor_window)
        self.autor_button.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.lending_button = Button(self.master, text="Prestamos")#, command=self.add_lending_window)
        self.lending_button.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.devolution_button = Button(self.master, text="Devoluciones")#, command=self.add_devolution_window)
        self.devolution_button.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.fine_button = Button(self.master, text="Multas")#, command=self.add_fine_window)
        self.fine_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.users_button = Button(self.master, text="Usuarios")#, command=self.add_user_window)
        self.users_button.place(relx=0.5, rely=0.6, anchor=CENTER)