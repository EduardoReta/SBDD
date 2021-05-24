import re
from tkinter import *
from rich.console import Console
from rich import style
from tkinter import ttk
import tkinter as tk

class Show:

    def __init__(self, master, cursor):
        self.master = master
        self.cursor = cursor
        self.frame = Frame(self.master)
        self.master.geometry("1000x1000")

        # Obtener nombres de tablas que empiecen por tbl
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
        
        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = []

        for x in self.row_to_list:
            for y in x:
                if re.search('tbl\w+', y):
                    self.clean_row_list.append(y)

        self.label1 = Label(self.master, text="Lista de tablas.")
        self.label1.pack()

        self.db_tables = ttk.Combobox(self.master, state='readonly')
        self.db_tables['values'] = self.clean_row_list
        self.db_tables.current(0)
        self.db_tables.pack()

        self.label2 = Label(self.master, text="Mostrar columnas de tabla: ")
        self.label2.pack()

        self.v = tk.StringVar()
        self.db_input = Entry(self.master, textvariable=self.v)
        self.db_input.pack()

        self.button1 = Button(self.master, text="Aceptar", command=self.get_var_value)#, command=lambda : self.button_pressed.set("button pressed"))
        self.button1.pack()

        self.labelCENTER = Label(self.master, text="Mostrar columna: ")
        self.labelCENTER.pack()

        self.column = tk.StringVar()
        self.column_selected = Entry(self.master, textvariable=self.column)
        self.column_selected.pack()

        self.label4= Label(self.master, text="De tabla: ")
        self.label4.pack()

        self.table_value = tk.StringVar()
        self.table_input = Entry(self.master, textvariable=self.table_value)
        self.table_input.pack()

        self.button2 = Button(self.master, text="Mostrar", command=self.show_data)
        self.button2.pack()

        self.label5= Label(self.master, text="Mostrar tabla: ")
        self.label5.pack()

        self.show_table_value = tk.StringVar()
        self.show_table_input = Entry(self.master, textvariable=self.show_table_value)
        self.show_table_input.pack()

        self.button3 = Button(self.master, text="Mostrar", command=self.show_table)
        self.button3.pack()

        self.text_box = Text(self.master, width=500, height=300)
        self.text_box.pack()

    # Muestra las columnas y los registros.
    def show_table(self) -> None:
        self.text_box.delete(1.0, END)
        self.cursor.execute(f"SELECT * FROM {self.show_table_value.get()}")
        for column in self.cursor.description:
            self.text_box.insert(END, str(column[0]) + " | ")
        self.row_to_list = [row for row in self.cursor]

        for item in self.row_to_list:
            self.text_box.insert(END, "\n"+str(item)) 


    # Mostramos contenido de columna de acuerdo a la tabla y columna que se inserte
    def show_data(self) -> None:

        self.text_box.delete(1.0, END)
        self.cursor.execute(f"SELECT {self.column.get()} FROM {self.table_value.get()};")
        self.row_to_list = [row for row in self.cursor]
        self.text_box.insert(END, self.column.get()+"\n")
        for item in self.row_to_list:
            self.text_box.insert(END, str(item[0])+"\n")
        

    # Mostramos columnas de tabla que se inserte
    def get_var_value(self) -> None:

        self.text_box.delete(1.0, END)
        self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{str(self.v.get())}'")
        self.row_to_list = [row for row in self.cursor]
        for item in self.row_to_list:
            self.text_box.insert(END, str(item[3])+"\n")