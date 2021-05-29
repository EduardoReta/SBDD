import traceback
import re
from tkinter import *
import tkinter as tk
from tkinter import messagebox


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


        self.label2 = Label(self.master, text="Mostrar columnas de tabla: ")
        self.label2.pack()

        self.v = tk.StringVar()
        self.db_input = Entry(self.master, textvariable=self.v)
        self.db_input.pack()

        self.v.trace("w", self.validate1)

        self.button1 = Button(self.master, text="Aceptar", command=self.get_var_value, state='disabled')#, command=lambda : self.button_pressed.set("button pressed"))
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

        self.button2 = Button(self.master, text="Mostrar", command=self.show_data, state="disabled")
        self.button2.pack()

        self.column.trace("w", self.validate2)
        self.table_value.trace("w", self.validate2)


        self.label5= Label(self.master, text="Mostrar tabla: ")
        self.label5.pack()

        self.show_table_value = tk.StringVar()
        self.show_table_input = Entry(self.master, textvariable=self.show_table_value)
        self.show_table_input.pack()

        self.button3 = Button(self.master, text="Mostrar", command=self.show_table, state="disabled")
        self.button3.pack()

        self.show_table_value.trace("w", self.validate3)

        self.label6 = Label(self.master, text="---------------------")
        self.label6.pack()

        self.button4 = Button(self.master, text="Ver Catalogos", command=self.catalogos)#E, command=self.show_table)
        self.button4.pack()

        self.button5 = Button(self.master, text="Ver Tablas", command=self.tablas)
        self.button5.pack()

        self.text_box = Text(self.master, width=500, height=300)
        self.text_box.pack()

        self.text_box.delete(1.0, END)
        self.text_box.insert(END, "Tablas a modificar:\n")
        for item in self.clean_row_list:
            self.text_box.insert(END, "\t"+item[3:]+"\n")

    # Muestra las columnas y los registros.
    def show_table(self) -> None:

        try:
            self.text_box.delete(1.0, END)
            if self.show_table_value.get() == "":
                raise Exception

            print(self.show_table_value.get())

            self.val = self.show_table_value.get()
            self.upper_val = str(self.val).upper()
            self.tbl_upper_val = "tbl"+self.upper_val

            self.cursor.execute(f"SELECT * FROM {self.tbl_upper_val}")
            for column in self.cursor.description:
                self.text_box.insert(END, str(column[0]) + " | ")
            self.row_to_list = [row for row in self.cursor]

            for item in self.row_to_list:
                self.text_box.insert(END, "\n"+str(item))

        except:
            # raise Exception
            messagebox.showinfo(message=f"Valor no valido")


    # Mostramos contenido de columna de acuerdo a la tabla y columna que se inserte
    def show_data(self) -> None:

        try:
            # print("ESTO", self.upper, self.upper_col)

            if self.column.get() == "" or self.table_value.get() == "":
                raise Exception
            
            if type(self.column.get()) == int or type(self.table_value.get()) == int:
                raise Exception


            

            self.tbl_value = self.table_value.get()
            self.upper_tbl_value = str(self.tbl_value).upper()
            self.upper = "tbl"+self.upper_tbl_value

            self.col_val = self.column.get()
            self.upper_col = str(self.col_val).upper()

            self.clean_row_list1 = []

            self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{str(self.upper)}'")
            self.row_to_list1 = [row for row in self.cursor]


            for item in self.row_to_list1:
                self.clean_row_list1.append(item[3])


            # for item in self.row_to_list1:
            #     self.text_box.insert(END, str(item[3])+"\n")

            print("estoo", self.clean_row_list1)

            if str(self.upper_col) not in self.clean_row_list1:
                raise Exception




            self.text_box.delete(1.0, END)
            self.cursor.execute(f"SELECT {self.upper_col} FROM {self.upper};")
            self.row_to_list = [row for row in self.cursor]
            self.text_box.insert(END, self.upper_col+"\n \n")
            for item in self.row_to_list:
                self.text_box.insert(END, str(item[0])+"\n")

            self.column_selected.delete(0, 'end')    

            self.table_input.delete(0, 'end')


        except:
            messagebox.showinfo(message=f"Valor no valido")
            # print(traceback.format_exc())

            self.db_input.delete(0, END)
            self.column_selected.delete(0, END)
            self.table_input.delete(0, END)
            self.show_table_input.delete(0, END)


    # Mostramos columnas de tabla que se inserte
    def get_var_value(self) -> None:

        try:

            if self.v.get() == "":
                raise Exception

            if type(self.v.get()) == int:
                raise Exception
            

            self.string = self.v.get()
            self.upper_tbl = "tbl"+self.string.upper()
            print(self.upper_tbl)

            self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
            
            self.row_to_list = [row for row in self.cursor]

            # Lista con el nombre de las puras tablas
            self.clean_row_list = []

            for x in self.row_to_list:
                for y in x:
                    if re.search('tbl\w+', y):
                        self.clean_row_list.append(y)

            print(self.clean_row_list)

            if self.upper_tbl not in self.clean_row_list:
                raise Exception

            self.text_box.delete(1.0, END)
            try:
                    self.cursor.execute(f"SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{str(self.upper_tbl)}'")
                    self.row_to_list = [row for row in self.cursor]

            except:
                    raise Exception

            for item in self.row_to_list:
                self.text_box.insert(END, str(item[3])+"\n")

        except:
            messagebox.showinfo(message=f"Valor no valido")


    def validate1(self, *args):
        if self.v.get():
            self.button1.config(state="normal")

        else:
            self.button1.config(state="disabled")

    def validate2(self, *args):
        if self.column.get() and self.table_value.get():
            self.button2.config(state="normal")

        else:
            self.button2.config(state="disabled")

    def validate3(self, *args):

        if self.show_table_value.get():
            self.button3.config(state="normal")
        
        else:
            self.button3.config(state="disabled")


    def catalogos(self):
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'cat%'")
        
        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = []

        for x in self.row_to_list:
            for y in x:
                if re.search('cat\w+', y):
                    self.clean_row_list.append(y)


        self.text_box.delete(1.0, END)
        for item in self.clean_row_list:
            self.cursor.execute(f"SELECT * FROM {item}")
            self.text_box.insert(END, str(item)+"\n")
            for row in self.cursor:
                self.text_box.insert(END, str(row)+"\n")
            self.text_box.insert(END, "\n")


    def tablas(self):
        self.cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE 'tbl%'")
        
        self.row_to_list = [row for row in self.cursor]

        # Lista con el nombre de las puras tablas
        self.clean_row_list = []

        for x in self.row_to_list:
            for y in x:
                if re.search('tbl\w+', y):
                    self.clean_row_list.append(y)


        self.text_box.delete(1.0, END)
        self.text_box.insert(END, "Tablas:\n")
        for item in self.clean_row_list:
            self.text_box.insert(END, "\t"+item+"\n")